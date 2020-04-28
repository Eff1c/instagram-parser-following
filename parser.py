import instaloader
from os import getcwd

L = instaloader.Instaloader()

L.load_session_from_file("cmvkdvldvclvxv@gmail.com", "/home/eff1c/project/first_parser/freelance/session")

profile = instaloader.Profile.from_username(L.context, "eff1c") # nickname of the person whose page you want to analyze


following = [followee for followee in profile.get_followees()]

followers = [follower for follower in profile.get_followers()]

unfollow = list(set(following) - set(followers))
output = []
for i in unfollow:
	href = str(i).split()[1]
	output.append("<p><a href='https://www.instagram.com/" + href + "/' target='_blank'>" + href + "</a></p>")

with open("list_unfollow.html", "w") as f:
	f.write("\n\n".join(output))

print("file://" + getcwd() + "/list_unfollow.html")
