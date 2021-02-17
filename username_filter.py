old_user = []
new_user = []
i = input("Input file: ")
of = input("Output file: ")
usernames = open(i, "r").read().splitlines()
for user in usernames:
    if user in old_user:
        print ("Username " + user + " ada yang sama, skip")
    else:
        new_user.append(user)
        old_user.append(user)

o = open(of, "w")
for user in new_user:
    o.write(user + "\n")
o.close()