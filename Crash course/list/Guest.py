Guest_list=['Harry Potter', 'Manuel', 'Gideon']
message="Please come over for dinner "
new_guess="Changed the guess name to"
more_guess="We found a reserved a much larger table We can invite more people now "
notable="no table are available "
nextime="They were trolling us let's meet next time "
stillinvited="Please come "
last="we have successfully finished this activity "
print(Guest_list[0], message)
print(Guest_list[1], message)
print(Guest_list[2], message)
print(Guest_list[2], "is Unable to come")

Guest_list[2] = "Ralph"
print(new_guess, Guest_list[2], "\n")
print(more_guess)

Guest_list.insert(0, "Tinkerbell") #adds tinkerbell at the beginning of the list
Guest_list.insert(2, "Sherlock") #adds tinker bell at the middle of the list
Guest_list.append("John")

for x in range(len(Guest_list)):
    print(Guest_list[x], message) #prints guess on a loop

print("\n")
'''without using loops
print(*Guest_list, message, sep= "\n")'''
print(notable)

while len(Guest_list) >= 3: 
    lessguess = Guest_list.pop() #checks and removes people from the guess list 1 b y 1
    print(lessguess, nextime) 

for x in range(len(Guest_list)):
    print(Guest_list[x], stillinvited) #invites the last 2 people left

while len(Guest_list) >= 1:
    del Guest_list[0]
print(Guest_list, last)

