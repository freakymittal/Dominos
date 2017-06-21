import requests

# #Get Session_id
# session = requests.Session()
# session.cookies.get_dict()
# {}
# response = session.get('https://pizzaonline.dominos.co.in')
# session_id = session.cookies.get_dict()['session_id']
# print(session_id)

payload = {
	'cardNumber[]' : '434',
	'isAjaxRequest' : 'json',
	'balanceInfoFlag': '1'	
}
r = requests.post('pizzaonline.dominos.co.in/payment/getbalanceinfo', params=payload)
print(r.text)