import requests

url ='http://10.10.10.128/dvwa/login.php'
#headers = {'user-agent': 'btk-akademi/1.1.1'}
data = {'usesrname':'admin','password':'password','Login':'Login'}
try:
    r = requests.post(url, data=data, allow_redirects=True,timeout=5)
    print(r.status_code)
    print(r.text)
    #print(r.headers)
    #print(r.headers.get('Date'))
except Exception as e:
    print(e)
    pass
