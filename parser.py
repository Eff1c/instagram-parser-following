import instaloader

L = instaloader.Instaloader()

L.login("login", "password")

profile = instaloader.Profile.from_username(L.context, "nickname") # nickname of the person whose page you want to analyze

following = []
for followee in profile.get_followees():
    following.append(followee.username)

followers = []
for follower in profile.get_followers():
    followers.append(follower.username)

output = list(set(following) - set(followers))
for i in output:
    print("https://www.instagram.com/" + i + "/")