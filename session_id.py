import requests
session = requests.Session()
session.cookies.get_dict()
{}
response = session.get('https://pizzaonline.dominos.co.in')
session_id = session.cookies.get_dict()['session_id']
print(session_id)