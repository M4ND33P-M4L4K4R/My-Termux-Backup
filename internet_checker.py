import requests
try:
    conn=requests.get("https://www.youtube.com")
    print('Connected')
except:
    print('Not connected')

