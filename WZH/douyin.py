import requests
import json
import csv

lists=[]
headers={
    "Accept-Encoding":"gzip",
    "Cache-Control":"max-stale=0",
    "Host":"api.amemv.com",
    "Connection":"Keep-Alive",
    "Cookie":"odin_tt=82a949aa8ae1b872fa4df2f60c4d33fec8f334b767602b8b60ef9f507d93b15d5e8647968ff313460faa0076256aaace",
    "User-Agent":"okhttp/3.8.1",
}
headers1={
"Accept-Encoding":"gzip",
"Cache-Control":"max-stale=0",
"Host":"aweme.snssdk.com",
"Connection":"Keep-Alive",
"Cookie":"odin_tt=82a949aa8ae1b872fa4df2f60c4d33fec8f334b767602b8b60ef9f507d93b15d5e8647968ff313460faa0076256aaace; qh[360]=1; install_id=40848822342; ttreq=1$e8c1f361efcda12544370f7a494603a452732861",
"User-Agent":"okhttp/3.8.1",
}
for i in range(8):
    url="https://api.amemv.com/aweme/v1/music/aweme/?music_id=6572842239368628996&cursor=%d&count=20&type=6&retry_type=no_retry&iid=40848822342&device_id=56150513062&ac=wifi&channel=wap_aweme_homepage&aid=1128&app_name=aweme&version_code=176&version_name=1.7.6&device_platform=android&ssmix=a&device_type=MI+6+&device_brand=Xiaomi&language=zh&os_api=19&os_version=4.4.2&uuid=863254010282712&openudid=1c1b0d1f9c475224&manifest_version_code=176&resolution=1280*720&dpi=240&update_version_code=1762&_rticket=1541749638586&ts=1541749638&as=a155933e1658fb5b354703&cp=3484b8526759e7bee1mqpf&mas=0079976b3ffd723983ff617d6724ae8a12cc0cec2caccc46ac4666 HTTP/1.1"%(i*20)
    # url="https://api.amemv.com/aweme/v1/user/?user_id=59595424956"
    # url="https://api.amemv.com/aweme/v1/user/?user_id=71628104519&retry_type=no_retry&iid=40848822342&device_id=56150513062&ac=wifi&channel=wap_aweme_homepage&aid=1128&app_name=aweme&version_code=176&version_name=1.7.6&device_platform=android&ssmix=a&device_type=MI+6+&device_brand=Xiaomi&language=zh&os_api=19&os_version=4.4.2&uuid=863254010282712&openudid=1c1b0d1f9c475224&manifest_version_code=176&resolution=1280*720&dpi=240&update_version_code=1762&_rticket=1541747089699&ts=1541747089&as=a105439ea1691b01651063&cp=3792b7561e5eef1be1lifq&mas=00642bcd2ff19ec2ce0ca1f2836e1fff62cc6c0c8cac6c8c0c468c HTTP/1.1"

    html=requests.get(url,headers=headers).text
    b=json.loads(html)
    for n in range(15):
        new_url="https://api.amemv.com/aweme/v1/user/?user_id=%s&retry_type=no_retry&iid=40848822342&device_id=56150513062&ac=wifi&channel=wap_aweme_homepage&aid=1128&app_name=aweme&version_code=176&version_name=1.7.6&device_platform=android&ssmix=a&device_type=MI+6+&device_brand=Xiaomi&language=zh&os_api=19&os_version=4.4.2&uuid=863254010282712&openudid=1c1b0d1f9c475224&manifest_version_code=176&resolution=1280*720&dpi=240&update_version_code=1762&_rticket=1541774858486&ts=1541774856&as=a1e5d9ee08905bce154337&cp=9303b5538b57eaede1kjmt&mas=0045c1713eb5e0589ef116f3d71fecf90aeccccc2cac8ca6c646ac HTTP/1.1"%(b['aweme_list'][n]['author_user_id'])
        new_html=requests.get(new_url,headers=headers1).text
        c=json.loads(new_html)
        print(c)
        nickname=c["user"]["nickname"]
        number=c["user"]["short_id"]
        signature=c["user"]["signature"]
        birthday=c["user"]["birthday"]
        total_favorited=c["user"]["total_favorited"]
        city=c["user"]["city"]
        fans_count=c["user"]["followers_detail"][0]["fans_count"]
        print(type(fans_count))
        # l=["抖音昵称："+nickname,"抖音ID:"+str(number),"生日:"+birthday,"个人简介:"+signature,"获赞数:"+str(total_favorited),"粉丝数:"+str(fans_count)]
        l=[nickname,str(number),city,birthday,signature,str(total_favorited),str(fans_count)]
        print(l)
        lists.append(l)

with open("douyin.csv", "w", encoding="utf-8",newline="") as f:
    k = csv.writer(f, dialect="excel")
    k.writerow(["抖音昵称", "抖音ID","城市" ,"生日", "个人简介", "获赞数", "粉丝数"])

    for list in lists:
        k.writerow(list)

