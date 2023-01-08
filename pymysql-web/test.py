import requests

# 注册测试
# url = 'http://127.0.0.1:7000/register'
# params = {"account_num": "2125488", "account_name": "xunjiangzee", "account_pass": "1234567", "entry_date":"2023-1-2"}
# result1 = requests.post(url, params=params)
# print(result1.text)

# # # 查询测试
# url = 'http://127.0.0.1:7000/get_info'
# params = {"account_name": "xunjiangze"}
# result2 = requests.get(url, params)
# print(result2.json())

# 登录测试
url = 'http://127.0.0.1:7000/login'
params = {"account_num": "2125488", "account_pass": "1234567"}
result3 = requests.get(url, params)
print(result3.text)
