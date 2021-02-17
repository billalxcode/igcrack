from instaloader import Instaloader
from instaloader import Hashtag
from instaloader import Profile
from instaloader import Post

i = input("Input file: ")
of = input("Output file: ")
old_user = []

logins = ["mjk02021", "majalengka"]
L = Instaloader()
L.login(logins[0], logins[1])

idx = 0
o = open(i, "r").read().splitlines()
saved = open(of, "a")
for user in o:
    profile = Profile.from_username(L.context, user)
    for follower in profile.get_followees():
        idx += 1
        print ("[ %d ] %s dumped" % (idx, follower.username))
        saved.write(follower.username + "\n")
saved.close()