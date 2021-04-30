'''Counting starts at 0'''

friends = ['Nickapic', 'Ben', 'Alex', 'Holsick']
'''print(friends[0]) #prints first item in the list
print(friends[1]) #prints 2nd item in the list
print(friends[2]) #prints 3rd item in the list
print(friends[3]) #prints 4th item in the list'''

mnic="Nickapic is a friend of mine that I got to know in INE "
mben="Ben is a friend of mine that I got to know in class3E "
malex="Alex is the one that told me to do this hands on and now here we are"
mholsick="holsick is one of the fastest learners that I've met and he is very creative"
question=input("which friend to you want to give a message too Nick(N), Ben(B), Alex(A), Holsick(H)? ")
nofriends="Nice imaginary friend "

if question.upper() == "N":
    print(mnic)
elif question.upper() == "B":
    print(mben)
elif question.upper() == "A":
    print(malex)
elif question.upper() == "H":
    print(mholsick)
else:
    print(nofriends)



