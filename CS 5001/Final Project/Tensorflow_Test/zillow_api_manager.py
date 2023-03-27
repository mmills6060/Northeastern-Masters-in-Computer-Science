import requests
import json
import os

max_results = 200
num_results = 0
results_per_page = 40
current_page = 1

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
            listing_price = listing['price']
            bathrooms = listing['bathrooms']
            bedrooms = listing['bedrooms']

            try:
                # Download the photo to a directory on your computer
                r = requests.get(photo_url, allow_redirects=True)

                # Check if the downloaded file is a JPEG
                if r.headers['Content-Type'] != 'image/jpeg':
                    raise Exception('Not a JPEG file')

                if r.content != b'none':  # check if the image is not "none"
                    filename = os.path.basename(photo_url)
                    with open('/Users/michaelmills/Pictures/Final_Project/' + filename, 'wb') as f:
                        f.write(r.content)
                    # Increment the number of listings processed
                    num_results += 1
                    # Print the listing price for debugging purposes
                    print(f"Processed listing #{num_results}: Price: ${listing_price} Bedrooms: {bedrooms} Bathrooms: {bathrooms}")
            except Exception as e:
                # Print an error message and continue to the next listing if an exception occurs
                print(
                    f"Error downloading photo for listing #{num_results}: {str(e)}")
                continue

        # Increment the current page number and update the query params
        current_page += 1
        query_params["page"] = current_page

        # Break out of the loop if we've reached the maximum number of results
        if num_results >= max_results:
            break

    else:
        # Print an error message if the API request was unsuccessful
        print(f"Error: {response.status_code}")
        break  # Exit the loop if the request failed

print(f"Processed a total of {num_results} listings.")
