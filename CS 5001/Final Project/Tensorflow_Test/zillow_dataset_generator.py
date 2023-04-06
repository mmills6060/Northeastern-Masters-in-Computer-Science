import requests
import json
import os
import pandas as pd
import tensorflow as tf
import csv


def define_variables_and_lists():
    max_results = 50000
    num_results = 0
    total_results = 0
    results_per_page = 40
    current_page = 1
    bed_input = 0
    bath_input = 0
    sort = "priorityScore"
    doz = 1
    no_results = False
    listings_per_page = 40
    num_page_results = 0
    
    # create empty lists to store values
    photo_urls = []
    listing_prices = []
    bathrooms_list = []
    bedrooms_list = []
    living_areas = []
    days_on_zillow = []
    zpids = []
    bathrooms = []
    bedrooms = []
    days_on_zillow_list = []
    return num_page_results, listings_per_page, max_results, no_results, num_results, total_results, results_per_page, days_on_zillow_list, current_page, photo_urls, listing_prices, bathrooms, bedrooms, living_areas, days_on_zillow, zpids, bed_input, bath_input, sort, doz, bathrooms_list, bedrooms_list




def get_Xb_Xb_sort_X_doz_X(num_page_results, listings_per_page, max_results, no_results, num_results, results_per_page, days_on_zillow_list , current_page, photo_urls, listing_prices, bathrooms, bedrooms, living_areas, days_on_zillow, zpids, total_results, bed_input, bath_input, sort, doz, bathrooms_list, bedrooms_list):
    print("Obtaining all listings that contain " + str(bed_input) + " bedroom and " + str(bath_input) + " bathroom, sorted by " + str(sort) + " and doz = " + str(doz) + "")
    num_results = 0
    # Set up the Zillow API endpoint and parameters
    url = "https://zillow56.p.rapidapi.com/search"
    query_params = {"location": "New York, NY",
                    "status": "forRent", "sort": sort, "beds_min": bed_input, "baths_min" : bath_input,"beds_max": bed_input, "baths_max": bath_input, "doz": doz, "page": current_page, "results_per_page": listings_per_page}

    headers = {
        "X-RapidAPI-Key": "62ab95a2e3msh3c57160cf27f53cp1c3f9ejsndaa8e5d8ea5f",
        "X-RapidAPI-Host": "zillow56.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=query_params)
        data = json.loads(response.content)
        total_result_count = data['totalResultCount']
        if total_result_count == 0:
            no_results = True  
    except:
        print("No results found for " + str(bed_input) + " bedroom and " + str(bath_input) + " bathroom, sorted by " + str(sort) + " and doz = " + str(doz) + "Page = " + str(current_page))
        no_results = True
    while num_results < total_result_count and no_results == False:
        response = requests.get(url, headers=headers, params=query_params)

    # Check if the response was successful
        if response.status_code == 200:
            # Parse the response JSON
            data = json.loads(response.content)
            total_result_count = data['totalResultCount']
            print("Amount of found listings: ", total_result_count)
            while num_results < total_result_count:
                
                # Extract the photo and listing price data for each listing
                for listing in data['results']:
                    num_results += 1
                    num_page_results += 1
                    if num_page_results == listings_per_page:
                        current_page += 1
                        num_page_results = 0
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
                    bathrooms_list.append(int(round(float(listing['bathrooms']))))
                    bedrooms_list.append(int(round(float(listing['bedrooms']))))
                    days_on_zillow_list.append(int(round(float(listing.get('daysOnZillow', -1)))))
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
                            
                            print(f"Processed listing #{num_results}: Price: ${listing_price} Bedrooms: {bedrooms} Bathrooms: {bathrooms} Square Feet: {living_area} Days on Zillow: {days_on_zillow} ZPID: {zpid} Page: {current_page}")
                    except Exception as e:
                        print(f"Error downloading photo for listing #{num_results}: {str(e)}")
                        
                        continue

        else:
            print(f"Error: {response.status_code}")
            break
    print(f"Processed a total of {num_results} listings.")
    total_results += num_results
    num_results = 0
    total_result_count = 0
    while no_results == False:
        # create a dataframe from the lists
        df = pd.DataFrame({
            'listing_price': listing_prices,
            'bathrooms': bathrooms_list,
            'bedrooms': bedrooms_list,
            'living_area': living_areas,
            'days_on_zillow': days_on_zillow_list,
        })

        # create a second dataframe from the lists
        df2 = pd.DataFrame({
            'imgSrc': photo_urls,
            'listing_price': listing_prices,
            'bathrooms': bathrooms_list,
            'bedrooms': bedrooms_list,
            'living_area': living_areas,
            'days_on_zillow': days_on_zillow_list,
            'zpid': zpids
        })
    

        # show the first 5 rows of the dataframe
        print("The first 5 rows of the dataframe looks like the following:")
        print(df.head())

        return df, df2
pass
def save_dataframe_to_csv(df, df2):
    print("writing dataframe to csv file")
    # define the file path and name
    file_path = "C:\\Users\\Michael Mills\\Documents\\Final Project\\Datasets\\zillow.csv"
    
    # save the DataFrame to a CSV file
    df.to_csv(file_path, index=False, header=False)

    # define the file path and name
    file_path2 = "C:\\Users\\Michael Mills\\Documents\\Final Project\\Datasets\\zillow.csv"

    # save the DataFrame to a CSV file
    df2.to_csv(file_path2, index=False, header=False)
    # print a confirmation message
    print("Dataframe saved to zillow.csv")

def main():

    num_page_results, listings_per_page, max_results, no_results, num_results, total_results, results_per_page, days_on_zillow_list, current_page, photo_urls, listing_prices, bathrooms, bedrooms, living_areas, days_on_zillow, zpids, bed_input, bath_input, sort, doz, bathrooms_list, bedrooms_list = define_variables_and_lists()
    #zillow api is limited to 800 results per search even with using pagination techniques. 
    sort = "priorityScore"
    doz = "36m"
    bed_input = 0
    while bed_input <= 5:
        bath_input = 1
        while bath_input <= 5:
            try:
                df, df2 = get_Xb_Xb_sort_X_doz_X(num_page_results, listings_per_page, max_results, no_results, num_results, results_per_page,days_on_zillow_list,  current_page, photo_urls, listing_prices, bathrooms, bedrooms, living_areas, days_on_zillow, zpids, total_results, bed_input, bath_input, sort, doz, bathrooms_list, bedrooms_list)
            except Exception as e:
                print("No results found for this search")
                break
            bath_input += 1
        bed_input += 1
    save_dataframe_to_csv(df, df2)
if __name__ == "__main__":
    main()

