from pip._internal import main
main(['install', 'requests'])

import requests,json,datetime

session=requests.Session()
session.get("https://reservation.bupt.edu.cn/index.php/1600")
now=datetime.datetime.now()+datetime.timedelta(hours=8)
datestr=datetime.datetime.strftime(now,"%Y%m%d")
resp=session.get("https://reservation.bupt.edu.cn/index.php/API/Room/ajax_return_one_period_one_room_timestate?room_id=15415&datesList%5B%5D="+datestr)
decoder=json.JSONDecoder()
data=decoder.decode(resp.text)


max_people=list(map(int,list(data[datestr]['max_people'].values())))
already_reserve=list(map(int,list(data[datestr]['already_reserve'].values())))
for ind in range(len(max_people)):
    if max_people[ind]-already_reserve[ind]!=0:
    	raise Exception("New Appointment Avaliable Now!")


