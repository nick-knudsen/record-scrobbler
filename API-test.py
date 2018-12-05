# A program to authenticate the user with Discogs using Oauth2

#TODO:
# Automate callback url pasting
# Turn into class for calling from other scripts
# Convert keys to hidden environmental variables for security

from urllib import parse
import discogs_client
import webbrowser

# consumer key and consumer secret are application-specific strings
# generated by discogs
consumer_key = "JumzrdFQUamqVRRPICXr"
consumer_secret = "jeOddrXBlFjJWmVwBIuMPQQQ iELrcgFz"

callback_url = "http://nickknudsen.photography/recordscrobbler/authorization"

# a unique identifier for this application, handed to discogs
user_agent = "record_scrobbler_test-0.1"

# instantiate client object and pass parameters
client = discogs_client.Client(user_agent)
client.set_consumer_key(consumer_key, consumer_secret)

# pass consumer key and consumer secret to discogs via
# the token request URL. Returns request token and request token secret
token, secret, url = client.get_authorize_url(callback_url)

# open webpage for auth
webbrowser.open(url)

# for testing purposes only
current_url = (input("Paste the redirect url here:\n"))

# retrieve token and verifier
callback_url_qs = parse.urlparse(current_url)[4]
callback_dict = parse.parse_qs(callback_url_qs)
oauth_token = str(callback_dict['oauth_token'][0])
oauth_verifier = str(callback_dict['oauth_verifier'][0])

# use verifier to retrieve access token and secret
access_token, access_secret = client.get_access_token(oauth_verifier)

# instantiate user object
user = client.identity()

print("You are authenticated as {username}, AKA {name}".format(username=user.username, name=user.name))