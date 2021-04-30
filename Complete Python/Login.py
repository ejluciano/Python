import time
users = {}
status = ""

def mainMenu():
    global status
    status = input("Do you have a login account? y/n or q to quit ")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
    elif status == "q":
        quit()


def newUser():
    createLogin = input("Create a login name: ")
    if createLogin in users:
        print ("\n Login name already exist! \n")
    else:
        createPass = input("Create password: ")
        users[createLogin] = createPass
        print("\n User Created!")
        logins=open("/home/penguin/programming/python/logins.txt", "a")
        logins.write("\n" + createLogin + " " + createPass)
        logins.close()

def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")
    
    #check if user exists

    if login in users and users[login] == passw:
        print("\n Login Successful \n")
        print("User: ", login, "accessed the system on: ", time.asctime())
    else:
        print("\n User doesn't exist or wrong password")

