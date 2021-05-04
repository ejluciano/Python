def make_album(artistname, title, numberofsongs=None):
    albums = {
        "Title" : title,
        "Name"  : artistname,
        "Number of songs" : numberofsongs,
    }
    print(albums)
#make_album("Nick","goodsong")
#make_album("Nick","goodsong", 8)


while True:
    print("\n Please input artist name: type or press q to quit ")
    name = input("What is the artist name? ")
    if (name == "quit" or name == "q"):
        break
    song = input("which album? ")
    if (song == "quit" or song == "q"):
        break
    make_album(name, song)
    
