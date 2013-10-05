import urllib2
import psycopg2


theurl = 'http://opensensors.io/antisocial'
username = 'datascience'
password = 'london101'
# a great password

passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
# this creates a password manager
passman.add_password(None, theurl, username, password)
# because we have put None at the start it will always
# use this username/password combination for  urls
# for which `theurl` is a super-url

authhandler = urllib2.HTTPBasicAuthHandler(passman)
# create the AuthHandler

opener = urllib2.build_opener(authhandler)

urllib2.install_opener(opener)
# All calls to urllib2.urlopen will now use our handler
# Make sure not to include the protocol in with the URL, or
# HTTPPasswordMgrWithDefaultRealm will be very confused.
# You must (of course) use it when fetching the page though.

antisoc = urllib2.urlopen(theurl).read()
# authentication is now handled automatically for us


# Set up Postgres Conn
try:
    conn = psycopg2.connect("dbname='assets' user='postgres' host='localhost' password=''")
except:
    print "I am unable to connect to the database"

# Define cursor
cur = conn.cursor()

anticsocdata = antisoc.splitlines()

del anticsocdata[0]
statements = ()
for row in anticsocdata:
    # split each row into a list
    rec = row.split(",")
    # if vomit is yes then 
    if(rec[0].lower() == "yes"): 
        cur.execute("""INSERT INTO assets_unity (lat, lon, seconds, type, quantity) VALUES (%s, %s, %s, %s, %s);""", (float(rec[2]), float(rec[9]), int('1'), 'vomit', int(1)))
        
    # if blood is yes then 
    if(rec[1].lower() == "yes"): 
        cur.execute("""INSERT INTO assets_unity (lat, lon, seconds, type, quantity) VALUES (%s, %s, %s, %s, %s);""", (float(rec[2]), float(rec[9]), int('1'), 'blood', int(1)))
    
    # if urine is yes then 
    if(rec[6].lower() == "yes"): 
        cur.execute("""INSERT INTO assets_unity (lat, lon, seconds, type, quantity) VALUES (%s, %s, %s, %s, %s);""", (float(rec[2]), float(rec[9]), int('1'), 'urine', int(1)))
        
    # if humanfouling is yes then 
    if(rec[6].lower() == "yes"): 
        cur.execute("""INSERT INTO assets_unity (lat, lon, seconds, type, quantity) VALUES (%s, %s, %s, %s, %s);""", (float(rec[2]), float(rec[9]), int('1'), 'humanfouling', int(1)))
    conn.commit()
        
       
    


