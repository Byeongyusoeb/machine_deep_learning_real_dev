import urllib.request


url = "http://uta.pw/shodou/img/28/214.png"
savename = "./download/test.png"

# Download

mem = urllib.request.urlopen(url).read() # Image file

with open(savename, mode = "wb") as f:
    f.write(mem)
    print("Saved")


# urllib.request.urlretrieve(url, savename) file save