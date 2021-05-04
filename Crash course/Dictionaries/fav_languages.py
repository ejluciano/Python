favorite_languages = {
    "EJ":"python",
    "Ben":"01101010",
    "nick":"Java",
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

for name in favorite_languages.keys():
    print(name.title())
    