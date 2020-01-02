
school_url =  'http://xjw.sdau.edu.cn/jwglxt/xtgl/login_slogin.html?language=zh_CN&_t='

CHOSE_COURSER_URL = "http://xjw.sdau.edu.cn/jwglxt/xsxk/zzxkyzb_xkBcZyZzxkYzb.html?gnmkdm=N253512&layout=default&su="

INDEX_URL = "http://xjw.sdau.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su="

logindata = {

    'yhm':None,  #用户名  自动抢课请填写
    'mm':None, #
    # 'mm':None,
    'v_yzm':'',
}

headers={

}

choseCoursePost = {
    "jxb_ids":None,
    #教学班ID
    "kch_id":None,
    #课程号
    "kcmc":"",
    #课程名称
    "rwlx":"2",
    #任务类型   --默认
    "rlkz":"0",
    #容量？？？？  --默认
    "rlzlkz":"0",
    #     --默认
    "sxbj":"0",
    #属性标记？？所选？？筛选 --默认
    "xxkbj":"0",
    #选修课标记？？  --默认
    "qz":"0",
    #强制？  --默认
    "cxbj":"0",
    #抽选标记？？
    "xkkz_id":"9AE177C17373D7C0E0536685C2CA0713",
    #选课课程ID
    "njdm_id":"2017",
    #年级代码   --默认
    "zyh_id":"006",
    #专业号ID
    "kklxdm":"15",
    #开课类型代码
    "xklc":"1",
    #选课流程 --默认？？？
    "xkxnm":"2019",
    #选课学年名 --默认
    "xkxqm":"12"
    #选课学期名--默认
}
