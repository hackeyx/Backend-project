# This code is to check the condition of the website.
import urllib.request

# enter the website url u wanna know its condition

url = "https://www.google.com"
this = urllib.request.urlopen(url).getcode()

if (this == 200):
    print("website working")
else:
    print("hmm :("
          "sorry website not working")

# oldest man (micheal!!!) 😂😂
