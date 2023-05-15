import requests
URL = 'https://dummyapi.io/data/v1'
session = requests.session()
body = {
   "firstName": "Jason",
   "lastName": "Liu",
   "email": "jason2@gmail.com"
}
r = session.request("post", f'{URL}/user/create', json=body, headers={'app-id': '63eb435ad8bb0b7ee5b67a77'})

print(r.json())
id = r.json()["id"]
print('id: ',id)

body = {
    "text": "test",
    "image": "string(url)",
    "likes": "30",
    "tags": "array(string)",
    "owner": "string(User id)"
}
r = session.request("post", f'{URL}/post/create', json=body, headers={'app-id': '63eb435ad8bb0b7ee5b67a77'})

