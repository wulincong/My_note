#___author:wulin___
#date:2019/11/24 0024

import requests
import time
import re
import UserInfo
import json

LOGIN_DATA = UserInfo.logindata
SCHOOL_URL = UserInfo.school_url
CHOSE_COURSER_URL = UserInfo.CHOSE_COURSER_URL
INDEX_URL = UserInfo.INDEX_URL
CHOSE_COURSE_POST = UserInfo.choseCoursePost
EACH_GRAB_TIMES = 10
OK = 1
ERROR = 0

def main():

    if not login():exit()
    if not CHOSE_COURSE_POST["jxb_ids"]:
        print("您还未选择课程，请按下面流程选课")
        while not getSourse():pass
    print("已完善所有信息，开始自动抢课")
    flag = EACH_GRAB_TIMES
    while flag:
        if grabCourse():
            print('恭喜选课成功')
            break
        else:time.sleep(0.1)
        flag -= 1
    if flag == 0:return 0
    return 1

def GetUserInfo():
    id = input('请输入学号>>>');LOGIN_DATA['yhm'] = id
    mm = input('请输入密码>>>');LOGIN_DATA['mm'] = [mm,mm]
    return id

def login():
    global se
    se = requests.session()
    URL = SCHOOL_URL + str(int(time.time()*1000))
    try:
        first_request = se.get(URL,timeout = 5)
    except:
        print("请检查网络环境，请在校园内网范围使用")
        return 0
    print('first request OK!')
    if not LOGIN_DATA['yhm']:
        print('请输入个人信息')
        GetUserInfo()
    else:
        print('您已经完善了登陆信息，下面会直接开始抢课')
    data = first_request.content.decode('utf-8')
    #完善请求头
    se.headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    se.headers["Accept-Language"] = "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
    se.headers["Cache-Control"] = "max-age=0"
    se.headers["DNT"] = "1"
    se.headers['Host'] = "xjw.sdau.edu.cn"
    se.headers['Referer'] = "http://xjw.sdau.edu.cn/jwglxt/xtgl/index_initMenu.html"
    se.headers["Upgrade-Insecure-Requests"] = "1"
    se.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.1.1.1'
    #csrftoken
    LOGIN_DATA['csrftoken'] = re.search('name="csrftoken" value="(.*?)"/>', data).group()[24:93]
    #登陆
    try:
        for i in range(3):
            data = se.post(URL,data=LOGIN_DATA)
            data = data.content.decode('utf-8')
            print('second requests OK')
            if "退出" in data:
                print("登陆成功")
                return 1
        print("请检查账号密码是否出错")
        return 0
    except:
        print("请检查网络环境或账号密码是否出错")
        return 0

def getSourse():
    sourse_name = input('请输入课程名>>>')
    f = open('sourse_list.json','r',encoding = 'utf8')
    data = json.load(f)
    f.close()
    class_list = []
    kch_id = 0
    for i in data:
        if i["kcmc"] == sourse_name:
            kch_id = i["kch_id"]
            class_list.append(i["jxbmc"])
            print(i["jxbmc"])
    if not class_list:
        print("课程未收录，请重新选择或自定义请求")
        return 0
    class_id = int(input('你选择第几个教学班>>'))-1
    print('您选择的教学班是',class_list[class_id])
    return getClassID(kch_id,class_id)

def getClassID(kch_id,class_id):
    import json
    post_data = {
        'rwlx': 2,
        'xkly': 0,
        'bklx_id': 0,
        'xqh_id': '002',
        'jg_id': '001',
        'zyh_id': '006',
        'zyfx_id': 'wfx',
        'njdm_id': 2017,
        'bh_id': '201700617-1',
        'xbm': 1,
        'xslbdm': 'wlb',
        'ccdm': 'w',
        'xsbj': 4294967296,
        'sfkknj': 0,
        'sfkkzy': 0,
        'sfznkx': 0,
        'zdkxms': 0,
        'sfkxq': 1,
        'sfkcfx': 0,
        'kkbk': 0,
        'kkbkdj': 0,
        'xkxnm': 2019,
        'xkxqm': 12,
        'rlkz': 0,
        'kklxdm': 10,
        'kch_id': kch_id,
        'xkkz_id': '9AD92B9332FDEF5FE0536785C2CA2BB0',
        'cxbj': 0,
        'fxbj': 0,
    }
    if 'XT' in kch_id:
        post_data['kklxdm'] = 15
        post_data['xkkz_id'] = '9AE177C17373D7C0E0536685C2CA0713'
    url = 'http://xjw.sdau.edu.cn/jwglxt/xsxk/zzxkyzb_cxJxbWithKchZzxkYzb.html?gnmkdm=N253512&su=' + LOGIN_DATA['yhm']  # 获取课程列表

    data = se.post(url, data=post_data)
    data = data.content.decode('utf-8')
    try:
        data = json.loads(data)[class_id]
    except:
        print("请重新选择正确的课程名和教学班")
        return 0
    classId = data['do_jxb_id']
    # print(classId)
    CHOSE_COURSE_POST["kch_id"] = kch_id
    CHOSE_COURSE_POST["jxb_ids"] = classId
    return 1

def grabCourse():
    url = 'http://xjw.sdau.edu.cn/jwglxt/xsxk/zzxkyzb_xkBcZyZzxkYzb.html?gnmkdm=N253512&su=' + LOGIN_DATA['yhm']
    data = se.post(url, data=CHOSE_COURSE_POST)
    data = data.content.decode('utf-8')
    data = json.loads(data)
    if not data:
        print("服务器返回数据为空，请检查请求头")
        return ERROR
    if data["flag"] == "1":return 1
    msg = data["msg"]
    if msg == "一门课程只能选一个教学班，不可再选！":
        print(msg)
        return OK
    print(msg)
    return 0

if __name__ == '__main__':
    print('欢迎使用教务系统助手')
    while 1:
        if main():exit()

