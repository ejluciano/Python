users = ["admin", "john", "man", "daemon", "dale"]
madm =("Would you like a status report? ")
mgen =("Why are you even here? ")
login =input("who are you? ")
if login.lower() == "admin":
    print(madm)
else:
    print(login, mgen)