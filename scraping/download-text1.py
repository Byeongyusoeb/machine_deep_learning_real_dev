import urllib.request


url = "https://api.aoikujira.com/ip/ini"

# Download

mem = urllib.request.urlopen(url).read()

print(mem.decode("utf-8"))