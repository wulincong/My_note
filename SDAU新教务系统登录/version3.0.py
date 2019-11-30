#___author:wulin___
#date:2019/11/24 0024

import requests
import time
import re
import UserInfo

LOGIN_DATA = UserInfo.logindata
SCHOOL_URL = UserInfo.school_url

def main():
    #第一次请求，并保存cookie到session会话
    print('欢迎使用URP教务系统助手')
    login()

def GetUserInfo():
    id = input('请输入学号>>>');LOGIN_DATA['yhm'] = id
    mm = input('请输入密码>>>');LOGIN_DATA['mm'] = [mm,mm]

def login():
    global se
    se = requests.session()
    URL = SCHOOL_URL + str(int(time.time()*1000))
    first_request = se.get(URL,timeout = 10)
    print('first request OK!')
    if not LOGIN_DATA['yhm']:
        print('请输入个人信息')
        GetUserInfo()
    data = first_request.content.decode('utf-8')
    # print(data)
    # print(csrftoken)
    # f = open('first.html', 'w', encoding='utf8')
    # f.write(first_request.content.decode('utf-8'))
    # f.close()
    # print(first_request.headers)
    # print(se.headers)
    # print(first_request.headers)
    se.headers['Cookie'] = first_request.headers['Set-Cookie'].strip(' Path=/jwglxt; HttpOnly')
    LOGIN_DATA['csrftoken']  = re.search('name="csrftoken" value="(.*?)"/>',data).group()[24:93]
    # print(se.headers['Cookie'])
    se.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.1.1.1'
    print(se.headers)
    data = se.post(URL,data=LOGIN_DATA)
    data = data.content.decode('utf-8')
    print('second requests')
    print(data)
    f = open('登陆.html', 'w', encoding='utf8')
    f.write(data)
    f.close()

if __name__ == '__main__':
    main()

