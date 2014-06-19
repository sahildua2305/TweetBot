import time
from TwitterAPI import TwitterAPI
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs

# application's key and key secret
ck = ''
cs = ''

# obtain request token
oauth = OAuth1(ck, cs)
r = requests.post(url='https://api.twitter.com/oauth/request_token', auth=oauth)
credentials = parse_qs(r.content)
request_key = credentials.get('oauth_token')[0]
request_secret = credentials.get('oauth_token_secret')[0]

#obtain authorization from twitter user
print('Visit this link to authorize the TweetBot:\n https://api.twitter.com/oauth/authorize?oauth_token=%s' % request_key)
verifier = raw_input('Enter your verification code: ')

# obtain access token
oauth = OAuth1(ck, cs, request_key, request_secret, verifier=verifier)
r = requests.get(url='https://api.twitter.com/oauth/access_token', auth=oauth)
credentials = parse_qs(r.content)
tk = credentials.get('oauth_token')[0]
ts = credentials.get('oauth_token_secret')[0]

# access TwitterAPI with the obtained access
api = TwitterAPI(ck, cs, tk, ts)
f = open('tweetbot.txt', 'rU')
for line in f:
    r = api.request('statuses/update', {'status' : line})
    print line,
    print r.status_code
    time.sleep(600)

