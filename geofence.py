import requests
import json

#UW= 200 University Avenue W, Waterloo, ON
#UofT= 40 St. George Street, Toronto, ON

def get_user_location():
    query = input("Enter a location: ")
    # query = "240 King Street W"
    url = "https://api.radar.io/v1/geocode/forward"
    query_params = {
        "query": query
    }
    headers = {
        "Authorization": "prj_test_pk_d178107c4163dfb942974e7a5c1f9974e76115af"
    }


    response = requests.get(url, params=query_params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    


def check_geofence(user_location):
    user_coordinates = ""
    user_coordinates = str(user_location['latitude']) + "," + str(user_location["longitude"])
 
    url = "https://api.radar.io/v1/search/geofences"
    query_params = {
        "near": user_coordinates
    }
    headers = {
        "Authorization": "prj_test_pk_d178107c4163dfb942974e7a5c1f9974e76115af"
    }

    response = requests.get(url, params=query_params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")


def main():

    # Get the user's current location from the Radar API
    user_location = get_user_location()
  
    if user_location:
        user_coordinates = { "latitude": user_location['addresses'][0]['latitude'],
        "longitude": user_location['addresses'][0]['longitude']}


    else:
        print("Failed to get user location.")

    geofence = check_geofence(user_coordinates)

    if geofence:
        if len(geofence['geofences']) != 0:
            print(geofence['geofences'][0]['description'], "geofence found")
        else:
            print("No geofence found!")

    else:
        print("Failed to get geofence")


if __name__ == "__main__":
    main()

