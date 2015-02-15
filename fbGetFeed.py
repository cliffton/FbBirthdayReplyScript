import requests
access= {'access_token':'CAACEdEose0cBAA25lw4mNhm4EvOp4h5U54E6FcMEYiGJNE39vHdcvDNMUubdGaA9XfHNQ8o0Xpah2pXxMouP65xHlfcaPDHSGXBFe4fZCsjnh66h3v2dlE3sUGhcc9zMbFkwEmcVhNWUasQ1rZBlwjt76ZClb8C3iH4V0nSV6GAZCBG7rajLFvaQZBNZBJH3kZD'}
payload={'access_token':'CAACEdEose0cBAA25lw4mNhm4EvOp4h5U54E6FcMEYiGJNE39vHdcvDNMUubdGaA9XfHNQ8o0Xpah2pXxMouP65xHlfcaPDHSGXBFe4fZCsjnh66h3v2dlE3sUGhcc9zMbFkwEmcVhNWUasQ1rZBlwjt76ZClb8C3iH4V0nSV6GAZCBG7rajLFvaQZBNZBJH3kZD','message':'test Comment'}
# status = requests.post('https://graph.facebook.com/cliffton/feed',params=payload)
feed = requests.get('https://graph.facebook.com/cliffton/feed',params=access)
#print(feed.json())
# print(status)
# print(response)
display = feed.json()
id = display['data'][0]['id']
print(id)

for c in range(0,100):
	send={'access_token':'CAACEdEose0cBAA25lw4mNhm4EvOp4h5U54E6FcMEYiGJNE39vHdcvDNMUubdGaA9XfHNQ8o0Xpah2pXxMouP65xHlfcaPDHSGXBFe4fZCsjnh66h3v2dlE3sUGhcc9zMbFkwEmcVhNWUasQ1rZBlwjt76ZClb8C3iH4V0nSV6GAZCBG7rajLFvaQZBNZBJH3kZD','message':'test Comment'+str(c)+''}
	comment = requests.post('https://graph.facebook.com/'+str(id)+'/comments',params=send)
	print('For'+ str(c) +' Comment'+ str(comment))


#SELECT message,post_id,created_time,permalink FROM stream where source_id=me() and actor_id!=me() and created_time<1356804073 and created_time>1356719491 limit 1000
