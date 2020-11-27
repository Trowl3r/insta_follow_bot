def read_txt(): 
    f = open("file.txt", "r")
    blacklist = []
    for x in f: 
        x = x.replace("\n", "")
        blacklist.append(x)

    return blacklist
    
read_txt()