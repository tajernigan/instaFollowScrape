import instaloader
import getpass
import json
# makes GET request to: https://i.instagram.com/api/v1/users/web_profile_info/?username=tajernigan

# get user info
USER = input("Enter Username: ")
PASSWORD = getpass.getpass("Enter Password: ")
# Get instance
L = instaloader.Instaloader()

L.login(USER, PASSWORD)

# Get profile of the user whose followers you want to download
profile = instaloader.Profile.from_username(L.context, USER)

# Get list of followers
print("Collecting Followers...")
followers = []
for follower in profile.get_followers():
    followers.append(follower.username)

# Get list of followees (accounts you are following)
print("Collecting Following...")
followees = []
for followee in profile.get_followees():
    followees.append(followee.username)

data = {
    "followers" : followers,
    "following" : followees
}

with open(USER + '.json', 'w') as json_file:
    json.dump(data, json_file)

print(f"Followers and followees saved to '{USER}.json'.") # creates a file based on your username
