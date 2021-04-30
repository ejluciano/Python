current_users = ["john", "levi", "leroi", "suc", "ada"]
sign_up =input("What user name do you want? ")

for current_user in current_users:
    if sign_up.lower() == current_user:
        print("Sorry it is unavailable")
    else:
        print("This user name is available ")
    break