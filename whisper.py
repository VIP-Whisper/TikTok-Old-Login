import requests
user='UserName'
psw='PassWord'
dev = '6785177577851504133'
iid = '7011916372695598854'
url = f'https://api2.musical.ly/passport/user/login/?mix_mode=1&username=&email=&mobile=&account=&password=&captcha=&ts=&app_type=normal&app_language=en&manifest_version_code=2018073102&_rticket=1633593458298&iid={iid}&channel=googleplay&language=en&fp=&device_type=SM-G955F&resolution=1440*2792&openudid=91cac57ba8ef12b6&update_version_code=2018073102&sys_region=AS&os_api=28&is_my_cn=0&timezone_name=Asia/Muscat&dpi=560&carrier_region=OM&ac=wifi&device_id={dev}&mcc_mnc=42203&timezone_offset=14400&os_version=9&version_code=800&carrier_region_v2=422&app_name=musical_ly&version_name=8.0.0&device_brand=samsung&ssmix=a&build_number=8.0.0&device_platform=android&region=US&aid=&as=&cp=Qm&mas='
head = {'user-agent':'okhttp'}
data = f'username={user}&password={psw}'
req = requests.post(url,headers=head,data=data)
if 'd_ticket' in str(req.cookies) and 'Maximum number of attempts reached. Try again later.' in str(req.text):
 print(f'[√] True')
elif 'Maximum number of attempts reached. Try again later.' in str(req.text):
 print(req.text)
else:
 print(req.text)