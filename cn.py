import requests,logging,random,time


def logging_init():
  # 创建一个logger对象
  logger = logging.getLogger('my_logger')
  logger.setLevel(logging.INFO)  # 设置日志级别为INFO

  # 创建一个控制台处理器，输出到控制台
  console_handler = logging.StreamHandler()
  console_handler.setLevel(logging.INFO)  # 设置控制台日志级别为INFO

  # 创建一个文件处理器，输出到文件
  file_handler = logging.FileHandler('test.log')
  file_handler.setLevel(logging.INFO)  # 设置文件日志级别为INFO

  # 创建一个日志格式化器
  formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
  console_handler.setFormatter(formatter)  # 给控制台处理器设置格式
  file_handler.setFormatter(formatter)  # 给文件处理器设置格式

  # 将控制台和文件处理器添加到logger
  logger.addHandler(console_handler)
  logger.addHandler(file_handler)
  return logger
logger = logging_init()
def getUA():
    safari_version = f'{random.randint(600, 700)}.{random.randint(1, 4)}.{random.randint(1, 5)}'
    ios_version = f'{random.randint(12, 15)}.{random.randint(0, 6)}.{random.randint(0, 9)}'
    ua_string = f'Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version} like Mac OS X) AppleWebKit/{safari_version} (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.20(0x16001422) NetType/WIFI Language/zh_CN'
    return ua_string
headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'authorization': 'null',
    'origin': 'https://cainiao220.top',
    'priority': 'u=1, i',
    'referer': 'https://cainiao220.top/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}
data = {
    'invite_code': '',
    'email_code': '',
    'email': '',
    'password': '11111111',
    'auth_password': '11111111',
    'recaptcha_data': '',
}

headers_clash ={
"User-Agent":"clash"
}


ua = getUA()
headers['user-agent'] = ua
account = ''
randomlength = 10
base_str = 'abcdefghijklmnopqrstuvwxyz0123456789'
length = len(base_str) - 1
for i in range(randomlength):
    account += base_str[random.randint(0, length)]
data['email'] = f"{account}@qq.com"
logger.info(data['email'])
response = requests.post('https://cainiao220.top/api/v1/passport/auth/register', headers=headers, data=data)
response = response.json()
logger.info(response)
token = response['data']['token']
clash_url = f"https://cainiao220.top/api/v1/client/subscribe?token={token}&flag=clash"
logger.info(clash_url)
response = ''
response = requests.get(clash_url,headers=headers)
with open('clash.yaml', 'w', encoding='utf-8') as file:
    file.writelines(response.text)




