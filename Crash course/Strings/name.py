name = input("Please type in your name here: ")
question = "would you like to learn some Python today?"
print(name, question)
print(name.upper(), question) #Creates an upper case version of name
print(name.lower(), question) #Creates a lower case version of name

quote="light shines in the dark: "
quotequestion=input("would you like a quote? y/n ")

if quotequestion == "y":
    print(quote)
else:
    print("dunno what you want")
