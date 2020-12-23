
#POST METHOD Spot workflow (GET RATE)

#load libraries to parse api request and json
import requests
import json

def api_request(url,payload,headers):
    '''
    This function defines the url,headers and payload below in order to send in a 
    api request to retrieve rate for this transaction (Buy USD and sell EUR).
    '''
    return response

url = "https://cambridge.com/api/344434/0/quotes/spot"

payload = '''
{'lockSide':'Payment', 
'settlementCurrency': 'EUR',
'amount': '60000',
'paymentCurrency': 'USD'}
'''

#demo environment at CMG accepts a cookie-based token that bypasses multi-factor authentication\
#instead of a bearer token to access this api resource
headers = {
  'Content-Type': 'application/json',
  'AccessToken': 'xxxxx' }

#Exception handling for robust api sourcing
try:
  response = requests.post(url, headers=headers, data = payload,timeout=5,allow_redirects = False)
  response.raise_for_status()

except requests.exceptions.HTTPError as HTTPErr:
    print(HTTPErr)
except requests.exceptions.ConnectionError as ConnectionErr:
    print(ConnectionErr)
except requests.exceptions.Timeout as TimeoutErr:
    print(TimeoutErr)
except requests.exceptions.RequestException as ExceptionsErr:
    print(ExceptionsErr)
    
#if-else statement to detect common errors
if response.status_Code == 400:
    print('Bad Request')
elif response.status_Code == 500:
    print('Internal Server Error')
else:
    print('StatusCode:' ,response.status_code,'Created')
    print('Headers:', response.headers["date"])

#Parse/Serialize JSON object within the response
new_string = json.loads(response.text)
print(json.dumps(new_string,ensure_ascii=False,indent = 2,sort_keys=True))

#access json_object using syntax: print(json_object['parentNode']['childNode])
print('quoteId: {} '.format(new_string['content']['quoteId']))

#access a content of the response. syntax: print(json_object['parent node']['child node])
print(new_string['content']['branchCode'])

#load a json file
with open('path_to_file/rates.text.json') as f:
    data = json.load(f)
print(data)

#save/download response in a json file in the directory
with open('rates.text','w') as json_file:
  json.dump(response,json_file)
