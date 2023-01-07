import requests

# # 注册测试
# url = 'http://127.0.0.1:5000/register'
# params = {"account_num": "2022212548", "account_name": "xunjiangze", "account_pass": "123456", "entry_date":"2023-1-2"}
# result1 = requests.post(url, params=params)
# #
# print(result1.text)

url = 'http://127.0.0.1:5000/get_info'
params = {"account_name": "xunjiangze"}
result2 = requests.get(url, params)
print(result2.json())
