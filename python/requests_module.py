import requests

good_url = "https://twitter.com/"
bad_url = "https://twitter.com/122333"

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0"

response = requests.get(good_url, headers=headers)

# grab the good url
if response.status_code == 200:
    print(response.content)
else:
    print("Failed to retrieve %s (%d)" % (good_url, response.status_code))

response = requests.get(bad_url, headers=headers)

# grab the good url
if response.status_code == 200:
    print(response.content)
else:
    print("Failed to retrieve %s (%d)" % (bad_url, response.status_code))
