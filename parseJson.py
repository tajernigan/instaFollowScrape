import json
import sys

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    raise TypeError("Provide the name of the JSON file created")

with open(file, "r") as json_file:
    data = json.load(json_file)

followers = data["followers"]
following = data["following"]

set_followers = set()
set_following = set()

for f in followers:
    set_followers.add(f)

for f in following:
    set_following.add(f)

print("accounts who don't follow you back:")
for f in following:
    if f not in set_followers:
        print(f)
print()

print("accounts you don't follow back: ")
for f in followers:
    if f not in set_following:
        print(f)
