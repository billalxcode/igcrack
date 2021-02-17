i = input("Input file: ")
splites = [".", "_"]
usernames = open(i, "r")
for user in usernames.read().splitlines():
    for splt in splites:
        if splt in user:
            try:
                x = user.split(splt)
                print (x)
            except ValueError:
                print (user)