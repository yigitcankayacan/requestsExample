import requests

# GET
get_url = "https://jsonplaceholder.typicode.com/todos"
get_response = requests.get(get_url)
# print(get_response.json())


# POST
to_do_item = {
    "userId": 2,
    "title": "my to do",
    "completed": False
}
post_url = "https://jsonplaceholder.typicode.com/todos"
post_response = requests.post(post_url, to_do_item)
# print(post_response.json())


# PUT__chance the item
to_do_item_15 = {'userId': 2, 'id': 15, 'title': 'put title', 'completed': False}
put_response = requests.put(get_url, json=to_do_item_15)
# print(put_response.json())


# DELETE
delete_response = requests.delete(get_url)
# print(delete_response.json())
