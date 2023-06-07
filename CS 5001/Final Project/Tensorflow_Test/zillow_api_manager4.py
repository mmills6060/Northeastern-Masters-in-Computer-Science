import requests
import json
import os
import pandas as pd
import tensorflow as tf


max_results = 680
num_results = 0
results_per_page = 40
current_page = 1

# create empty lists to store values
photo_urls = []
listing_prices = []
bathrooms = []
bedrooms = []
living_areas = []
days_on_zillow = []
zpids = []




# Set up the Zillow API endpoint and parameters
url = "https://zillow56.p.rapidapi.com/search"
query_params = {"location": "New York, NY",
                "status": "forRent", "page": current_page}

headers = {
    "X-RapidAPI-Key": "62ab95a2e3msh3c57160cf27f53cp1c3f9ejsndaa8e5d8ea5f",
    "X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

while num_results < max_results:
    response = requests.get(url, headers=headers, params=query_params)

# Check if the response was successful
    if response.status_code == 200:
        # Parse the response JSON
        data = json.loads(response.content)

        # Extract the photo and listing price data for each listing
        for listing in data['results']:
            photo_url = listing['imgSrc']
            listing_price = int(round(float(listing['price'])))
            bathrooms = int(round(float(listing['bathrooms'])))
            bedrooms = int(round(float(listing['bedrooms'])))
            living_area = int(round(float(listing.get('livingArea', -1)))) # Use -1 as default value if livingArea is missing or non-numeric
            days_on_zillow = int(round(float(listing.get('daysOnZillow', -1)))) # Use -1 as default value if daysOnZillow is missing or non-numeric
            zpid = int(round(float(listing.get('zpid', -1)))) # Use -1 as default value if zpid is missing or non-numeric
            photo_urls.append(listing['imgSrc'])
            listing_prices.append(int(round(float(listing['price']))))
            living_areas.append(int(round(float(listing.get('livingArea', -1)))))
            zpids.append(int(round(float(listing.get('zpid', -1)))))
          #  bathrooms.append(str(listing['bathrooms']))
         #   bedrooms.append(str(listing['bedrooms']))
         #   days_on_zillow.append(str(listing.get('daysOnZillow', None)))
            try:
                # Download the photo to a directory based on the listing price
                if 1000 <= listing_price < 2000:
                    directory = "C:\\Users\\Michael Mills\\Pictures\\Final Project\\Zillow\\1000"
                elif 2000 <= listing_price < 3000:
                    directory = "C:\\Users\\Michael Mills\\Pictures\\Final Project\\Zillow\\2000"
                elif 3000 <= listing_price < 4000:
                    directory = "C:\\Users\\Michael Mills\\Pictures\\Final Project\\Zillow\\3000"
                elif 4000 <= listing_price < 5000:
                    directory = "C:\\Users\\Michael Mills\\Pictures\\Final Project\\Zillow\\4000"
                elif 5000 <= listing_price < 6000:
                    directory = "C:\\Users\\Michael Mills\\Pictures\\Final Project\\Zillow\\5000"
                elif 6000 <= listing_price < 7000:
                    directory = "C:\\Users\\Michael Mills\\Pictures\\Final Project\\Zillow\\6000"
                elif 7000 <= listing_price < 8000:
                    directory = "C:\\Users\\Michael Mills\\Pictures\\Final Project\\Zillow\\7000"
                elif 8000 <= listing_price < 9000:
                    directory = "C:\\Users\\Michael Mills\\Pictures\\Final Project\\Zillow\\8000"
                elif 9000 <= listing_price < 10000:
                    directory = "C:\\Users\\Michael Mills\\Pictures\\Final Project\\Zillow\\9000"
                elif 10000 <= listing_price:
                    directory = "C:\\Users\\Michael Mills\\Pictures\\Final Project\\Zillow\\10000"

                r = requests.get(photo_url, allow_redirects=True)
                if r.headers['Content-Type'] != 'image/jpeg':
                    raise Exception('Not a JPEG file')

                if r.content != b'none':
                    filename = os.path.basename(photo_url)
                    with open(directory + '/' + filename, 'wb') as f:
                        f.write(r.content)
                    num_results += 1
                    print(f"Processed listing #{num_results}: Price: ${listing_price} Bedrooms: {bedrooms} Bathrooms: {bathrooms} Square Feet: {living_area} Days on Zillow: {days_on_zillow} ZPID: {zpid} ")
            except Exception as e:
                print(f"Error downloading photo for listing #{num_results}: {str(e)}")
                continue

        current_page += 1
        query_params["page"] = current_page

        if num_results >= max_results:
            break

    else:
        print(f"Error: {response.status_code}")
        break
print(f"Processed a total of {num_results} listings.")


# create a dataframe from the lists
df = pd.DataFrame({
    'listing_price': listing_prices,
    'bathrooms': bathrooms,
    'bedrooms': bedrooms,
    'living_area': living_areas,
    'days_on_zillow': days_on_zillow,
})

# create a second dataframe from the lists
df2 = pd.DataFrame({
    'imgSrc': photo_url,
    'listing_price': listing_prices,
    'bathrooms': bathrooms,
    'bedrooms': bedrooms,
    'living_area': living_areas,
    'days_on_zillow': days_on_zillow,
    'zpid': zpids
})
# show the first 5 rows of the dataframe
print("The first 5 rows of the dataframe looks like the following:")
print(df.head())

# define the file path and name
file_path = "C:\\Users\\Michael Mills\\Documents\\Final Project\\Datasets\\zillow.csv"

# save the DataFrame to a CSV file
df.to_csv(file_path, index=False, header=False)

# define the file path and name
file_path2 = "C:\\Users\\Michael Mills\\Documents\\Final Project\\Datasets\\zillow.csv"

# save the DataFrame to a CSV file
df2.to_csv(file_path, index=False, header=False)
# print a confirmation message
print("Dataframe saved to zillow.csv")

