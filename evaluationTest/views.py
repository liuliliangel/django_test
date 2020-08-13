from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import urllib.parse
# Create your views here.
from django.template.loader import get_template


def GetStudent(request):
    return render(request, 'GetStudent.html')


#获取学员信息
def GetStudentUid(card):
    getStuUid_url = "https://evaluation-beta.speiyou.com/diagnosis-api/test/queryUserByCode"
    header = {'Content-Type': 'application/x-www-form-urlencoded', 'platform': '3',
                 'utoken': 'eyJpdiI6Ijlud2JBWXQ1VGxKMm55YW9TU2Fsd3c9PSIsInZhbHVlIjoicDYzYzZWSUJzL1JIM3drbTdlOTB2MkpLSjNOeG15aFIvVVI2TmRKV3ZqTjdUd010bk5KckpOaTd6SnBIdnUzNG5YejdBbk5xeEdIWTVKUmdreW9sM0E9PSJ9'}

    r = requests.post(getStuUid_url, data=card, headers=header).json()
    # rvalue = json.load(r.text)
    #r ={'rlt': str(r.json())}
    # print("返回的数据类型：",type(r))
    # print(r.keys())
    # if not r["data"] is None:
    #     return {'rlt':str(r["data"]["data"]["cityList"][0]["uid"])}
    # else:
    #     return {'rlt':"学员编号为空或者不存在"}

    if  not r["data"] is None:
        if not r["data"]["code"] is None:
            # print("data的值：", r["data"]["code"])
            # print("code的值类型：", type(r["data"]["code"]))

            return str(r["data"]["data"]["cityList"][0]["uid"])
        else:
            return {'rlt': "学员编号不存在"}

    else:
        return {'rlt': "学员编号为空或者不存在"}

    # return r.json()

#获取加密的学员uid
def GetStudentjiamiUid(uid):
    getjiamiUid_url = "https://evaluation-beta.speiyou.com/diagnosis-api/test/getLoginUid"
    header = {'Content-Type': 'application/x-www-form-urlencoded', 'platform': '3',
                 'utoken': 'eyJpdiI6Ijlud2JBWXQ1VGxKMm55YW9TU2Fsd3c9PSIsInZhbHVlIjoicDYzYzZWSUJzL1JIM3drbTdlOTB2MkpLSjNOeG15aFIvVVI2TmRKV3ZqTjdUd010bk5KckpOaTd6SnBIdnUzNG5YejdBbk5xeEdIWTVKUmdreW9sM0E9PSJ9'}

    if not uid is None:
        r = requests.post(getjiamiUid_url, data=uid, headers=header).json()

        return  r["data"]
    else:
        return {'rlt':"学员uid为空，不存在"}


#获取短链接通过加密uid

def GetShortUidUrl(jiamiUidPra):
    getShortUrl = "https://s.speiyou.cn/compress"
    header = {'Content-Type': 'application/x-www-form-urlencoded', 'sign': 'MTY5NzIyMzYxMzYyNQ==.b95df3390ac43e6b613746d43078a984ac1c96c06ce49126bf1b67d64aa7376a',
                 'appId': 'novice-diagnosis'}
    jiamiUid = {}
    jiamiUid['encryptUid'] = jiamiUidPra
    #加密的uid进行urlencode编码
    urlencodeuid = urllib.parse.urlencode(jiamiUid)
    print("加密后的uid：",urlencodeuid)

    lenUrl = {}
    #拼接入参的url测试环境
    lenUrl['url'] = "https://evaluation-beta.speiyou.com/h5/introduced?"+urlencodeuid+"&cityCode=010&type=6"
    # print("自己拼接的URL入参：",lenUrl1)
    # lenUrl['url'] = "https://evaluation-beta.speiyou.com/h5/introduced?encryptUid=lrq86aw7AozYKJ5GyfgzxdeGtFk8zeA7sPuIlb1qyBvPO6GJbr6%2b&cityCode=010&type=6"

    r = requests.post(getShortUrl, data=lenUrl, headers=header)

    return {'rlt':str(r.json())}


# 获取学员Uid
def GetStudentShortUrl(request):
    stuCard = {}
    getUid = {}


    if request.POST:
        stuCard['card'] = request.POST['stuCard']
        print("输入的数据", stuCard)
        # print("获取的stucard的类型：",type(stuCard))

    getUid['uid'] = GetStudentUid(stuCard)
    print("获取的Uid为：",getUid['uid'])
    if getUid['uid'] is None:
        rlt = {'rlt':"学员不存在"}
    else:
        getjiamiUid = GetStudentjiamiUid(getUid)
    print("获取的加密Uid为：",getjiamiUid)

    rlt = GetShortUidUrl(getjiamiUid)

    #rlt = {'rlt': str(xinxi)}
    #rlt = json.dump(xinxi,fp= str,indent=2)
    print("dump后的返回数据类型：",type(rlt))
    print(rlt)
    return render(request, "GetStudent.html",rlt)


def hello(request):
    return HttpResponse("Hello world ! ")


# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
