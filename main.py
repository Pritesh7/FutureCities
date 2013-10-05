import urllib2
import postgres

password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

top_level_url = "http://opensensors.io/"

password_mgr.add_password(None, top_level_url, 'datascience', 'london101')

handler = urllib2.HTTPBasicAuthHandler(password_mgr)
# create "opener" (OpenerDirector instance)
opener = urllib2.build_opener(handler)

# use the opener to fetch a URL
opener.open('http://opensensors.io/')

# Install the opener.
# Now all calls to urllib2.urlopen use our opener.
urllib2.install_opener(opener)

this_url = 'http://opensensors.io/dogfouling'
print urllib2.urlopen(this_url).read()

