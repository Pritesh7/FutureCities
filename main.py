import urllib2
import psycopg2

#set connection data:
top_level_url = "http://opensensors.io/"
username = 'datascience'
password = 'london101'
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

password_mgr.add_password(None, top_level_url, username, password)

handler = urllib2.HTTPBasicAuthHandler(password_mgr)
# create "opener" (OpenerDirector instance)
opener = urllib2.build_opener(handler)
# use the opener to fetch a URL
opener.open('http://opensensors.io/')
# Install the opener.
# Now all calls to urllib2.urlopen use our opener.
urllib2.install_opener(opener)

#connect to the API:
try:
    conn = psycopg2.connect("dbname='FutureCities' user='postgres' host='localhost' password='a'")
    print "success"
except:
    print "I am unable to connect to the database"

#set cur connection for database:
cur = conn.cursor()

#pull in specific data:
dogshit = urllib2.urlopen('http://opensensors.io/dogfouling').read()
#split it into a list of lists:
allshit = dogshit.splitlines()
#remove header row:
del allshit[0]
print len(allshit)
for i , row in enumerate(allshit):
    #print row.split(',')[2]
    cur.execute("""INSERT INTO assets_unity (lat, lon, seconds, type, quantity) VALUES (%s, %s, %s, %s, %s);""",
        (float(row.split(',')[2]),
            float(row.split(',')[3]),
            int('1'),
            str('dogfoul'),
            int(1)))
    conn.commit()

# eventdata = lineitem[0]
# street = lineitem[1]
# lat = ineitem[2]
# long = lineitem[3]
# x = lineitem[4]
# y = lineitem[5]