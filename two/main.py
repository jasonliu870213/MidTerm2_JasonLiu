import requests
URL = 'https://dummyapi.io/data/v1'
session = requests.session()
body = {
   "firstName": "Jason",
   "lastName": "Liu",
   "email": "jason33@gmail.com"
}
r = session.request("post", f'{URL}/user/create', json=body, headers={'app-id': '63eb435ad8bb0b7ee5b67a77'})

print(r.json())
user_id = r.json()["id"]
print('id: ', user_id)

body = {
    "text": "test",
    "image": "image_url",
    "likes": "30",
    "tags": ['haha'],
    "owner": id
}
r = session.request("post", f'{URL}/post/create', json=body, headers={'app-id': '63eb435ad8bb0b7ee5b67a77'})
post_id = r.json()['id']
print('post id:', post_id)
