from fake_useragent import UserAgent
import requests,json
accouts=json.loads(open("./accouts.json", mode='r').read())
ua = UserAgent()
for i in accouts["sp"]:
	print("--------"+i["name"]+"----------")
	checkin_url=i["url"]["cu"]
	login_url=i["url"]["lu"]
	login_data={
				"email":i["ac"]["u"],
				"passwd":i["ac"]["p"]
				}

	headers={
			"user-agent":ua.random
			}
	print("User-Agent:",headers)
	lose=requests.Session()
	login_res=lose.post(login_url,data=login_data,headers=headers).content.decode("unicode-escape")
	checkin_res=lose.post(checkin_url,headers=headers).content.decode("unicode-escape")
	data_checkin=checkin_res
	print("Return Json:",data_checkin,"\n")
