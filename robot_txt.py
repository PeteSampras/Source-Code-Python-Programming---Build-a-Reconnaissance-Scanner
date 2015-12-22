import urllib.request
import urllib.error
import io

def get_robots_txt(url):

	if url.endswith('/'):
		path = url
	else:
		path = url + '/'
	
	try: req =  urllib.request.urlopen(path + "robots.txt", data= None)
	except urllib.request.HTTPError as e:
		return 'The server couldn\'t fulfill the request. '+'Error code: '+ str(e.code)
	except urllib.request.URLError as e:
		return 'We failed to reach a server. '+'Reason: '+ str( e.reason)
	else:
		data = io.TextIOWrapper(response, encoding = 'utf-8')
		return data.read()
	
	
	
#print(get_robots_txt('http://www.krucil.net/'))
	
