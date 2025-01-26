#see also geopy  doc at https://geopy.readthedocs.io/en/stable/
#see also timezonefinder doc at https://pypi.org/project/timezonefinder/

from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim

tf = TimezoneFinder()

points = [(13.358, 52.5061),(-71.057083, 42.361145), (-104.991531, 39.742043)]

for lng, lat in points:
    tz = tf.timezone_at(lng=lng, lat=lat)
    print(tz)

print()
geolocation = Nominatim(user_agent="photon")
loc = input("Please enter zipcode :")
cnt = input("Please enter country code:")
location = geolocation.geocode(loc + "," + cnt)
print(location)