import requests
r = requests.get("https://jsonplaceholder.typicode.com/users/2")
print(r.status_code)
print(r.headers["Content-Type"])
print(r.json()["name"])

r = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "test", "body": "x", "userId": 1},
)
print(r.status_code)
print(r.json())