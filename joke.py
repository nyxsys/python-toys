import urllib.request
filename, headers = urllib.request.urlretrieve('http://en.wikipedia.org/w/api.php?format=json&action=query&titles=India&prop=revisions&rvprop=content&callback=?')
response = open(filename)
print(response)
#json = eval(response.read())
#print(json)
