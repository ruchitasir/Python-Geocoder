# Import the module (top of the file).
import requests
import geocoder

destinations = ["The Space Needle",
  "Crater Lake",
  "The Golden Gate Bridge",
  "Yosemite National Park",
  "Las Vegas, Nevada",
  "Grand Canyon National Park",
  "Aspen, Colorado",
  "Mount Rushmore",
  "Yellowstone National Park",
  "Sandpoint, Idaho",
  "Banff National Park",
  "Capilano Suspension Bridge"]

YOUR_API_KEY_HERE = '538810c2465fd7b05700a1e5eb6ccffa'
# Make sure to replace [YOUR_API_KEY_HERE] with your actual key, which
# will look like a bunch of letters and numbers! Alternatively, copy the sample
# API call from Dark Sky dashboard and just remove the coordinates.
API_BASE_URL = "https://api.darksky.net/forecast/"+YOUR_API_KEY_HERE+"/"

# API_BASE_URL = "https://api.darksky.net/forecast/[538810c2465fd7b05700a1e5eb6ccffa]/"

# Previous code still here.

for point in destinations:
    # Previous `geopy` code still here.
    loc = geocoder.arcgis(point)
    full_api_url = API_BASE_URL + str(loc.latlng[0]) + "," + str(loc.latlng[1])
    result = requests.request('GET', full_api_url).json()
    #print('result',result['currently']['temperature'])
    print('result',result["currently"]["temperature"])
    # Both print works but if you use print(f"") then you have to use result['currently']['temperature'] instead of result["currently"]["temperature"]
    # From the result, print out the summary and current temperature.