from instaloader import Instaloader
from instaloader import Hashtag
from instaloader import Profile
from instaloader import Post

old_user = []
new_user = []
saved = open("subang.txt", "a")
user = input("Username: ")
pasw = input("Password: ")
L = Instaloader()
L.login(user, pasw)

idx = 0
for post in Hashtag.from_name(L.context, "majalengka").get_posts():
    idx += 1
    try:
        if post.profile in old_user:
            print ("[ %d ] %s skip" % (idx, post.profile))
        else:
            print ("[ %d ] %s dumped" % (idx, post.profile))
            old_user.append(post.profile)
            new_user.append(post.profile)
            saved.write(post.profile + "\n")
    except KeyboardInterrupt: break
saved.close()