import requests
import json
import csv
import os
from subprocess import Popen

##imported the libraries above 

url = "https://top-navigation.prod.crto.in/api/campaigns/getByEntity"

querystring = {"type":"Partner","id":"13149","status":"0,2"}

payload = ""
headers = {
    'Cookie': "uid=d7519dad-ae5d-4573-9ac0-50267bbf88d1; _ga=GA1.2.993796039.1543352556; cto_lwid=3b434de2-a613-40a6-a9b2-f6b5de587b83; _ceg.s=pj7zr6; _ceg.u=pj7zr6; ajs_user_id=%22105925%22; ajs_anonymous_id=%226927e8f3-ee69-42b9-8a29-7b8b4fad9aed%22; ajs_group_id=%221594%22; cto_axid=Q7YI0yWSrAkZul-uVni5W3n5nguqIOgb; h=%7b%22Pdp_v%22%3a%5b%5d%2c%22d%22%3a%7b%22m%22%3a%221%22%2c%22as_vpc%22%3a%22LvgW8w0r879kxcE7%2fMFdqacH1z6eT0etY6mO6Rzm1zs%3d%22%2c%22t_421%22%3a%22%2f5jP00YRl1A%3d%7c2018-12-11T18%3a10%3a46%22%7d%7d; _fbp=fb.1.1549404441259.2081440928; amplitude_idundefinedcriteo.com=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; mp_105bfc6513485ed4bb648d1b388d9989_mixpanel=%7B%22distinct_id%22%3A%20%22105925%22%2C%22%24device_id%22%3A%20%22167892da730719-041325df1355d2-35607400-1fa400-167892da73114c7%22%2C%22mp_lib%22%3A%20%22Segment%3A%20web%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fmarketing.criteo.com%2FLogin%3FredirectTo%3D%252F%22%2C%22%24initial_referring_domain%22%3A%20%22marketing.criteo.com%22%2C%22%24user_id%22%3A%20%22105925%22%2C%22mp_name_tag%22%3A%20%22105925%22%2C%22id%22%3A%20%22105925%22%7D; amplitude_id_b37a423901694056906133c8c13c895dcriteo.com=eyJkZXZpY2VJZCI6IjY4MThlNGE3LTk1MDktNGI4Yy05MzVlLTI5N2VkMmM4YjE2ZFIiLCJ1c2VySWQiOiIxMDU5MjUiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE1NDk5OTE0NzI3MDQsImxhc3RFdmVudFRpbWUiOjE1NDk5OTE1MjM2MjcsImV2ZW50SWQiOjIzLCJpZGVudGlmeUlkIjozNiwic2VxdWVuY2VOdW1iZXIiOjU5fQ==; _gid=GA1.2.2041778269.1550083569; _gat=1; JWT=eyJhbGciOiJSUzI1NiIsImtpZCI6InZGa1RZMl95THZMcnlQclFZRVlnaDJETGc3MGhMVjExSVdjV1pOcHY2RVEiLCJ0eXAiOiJKV1QifQ.eyJjdHg6dXNlcjpkaXNwbGF5TmFtZSI6Ikp1c3RpbmUgSmFmZmUiLCJjdHg6dXNlcjplbWFpbCI6ImouamFmZmVAY3JpdGVvLmNvbSIsImN0eDp1c2VyOnVpZCI6ImouamFmZmUiLCJjdHg6dXNlcjp1bXNJZCI6MTA1OTI1LCJjdHg6dXNlcjp3aW5Mb2dpbiI6ImouamFmZmUiLCJzbiI6IkphZmZlIiwibmFtZWlkIjoidTppOmouamFmZmVAY3JpdGVvLmNvbSIsImlhdCI6MTU1MDA5NTk5NCwiaXNzIjoiY3JpdGVvLXRvcCIsImV4cCI6MTU1MDE4MjQ1NCwibmJmIjoxNTUwMDk2MDU0fQ.abBnSy-ysH_n06y29kS8dCFqcwqLQ7SKZfVqiovz484gwV_u020JOwkd1xFBeQjPZVrfDSnTxFRppR8z_Cxlc1TLyeqekmsz1rCRw9FcFR09FwWALNNhF0zp3VbKKCiq6WZ4zNoMgHJ5QW23ojQHPoIhxLC7-RQXQn3VwyFQO3VKsgxn4jdXWzJ84qAjl9Lyyldoydx9ERURpXav_qJtYDjRZQFgPkZJ9zmvswH7hliWuAlV2gF_Ywo9xPZz2LXJTDNTsiKAUhvwlMT-J-U0q1khkAdkP6JaTDMriiEpov86qlvIhtnER2tOV41FprntJ8WYnO6P9lc9iUfm9omoBA",
    'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6InZGa1RZMl95THZMcnlQclFZRVlnaDJETGc3MGhMVjExSVdjV1pOcHY2RVEiLCJ0eXAiOiJKV1QifQ.eyJjdHg6dXNlcjpkaXNwbGF5TmFtZSI6Ikp1c3RpbmUgSmFmZmUiLCJjdHg6dXNlcjplbWFpbCI6ImouamFmZmVAY3JpdGVvLmNvbSIsImN0eDp1c2VyOnVpZCI6ImouamFmZmUiLCJjdHg6dXNlcjp1bXNJZCI6MTA1OTI1LCJjdHg6dXNlcjp3aW5Mb2dpbiI6ImouamFmZmUiLCJzbiI6IkphZmZlIiwibmFtZWlkIjoidTppOmouamFmZmVAY3JpdGVvLmNvbSIsImlhdCI6MTU1MDI2NTU0NCwiaXNzIjoiY3JpdGVvLXRvcCIsImV4cCI6MTU1MDM1MjAwNCwibmJmIjoxNTUwMjY1NjA0fQ.YqhR2F5-do8K3mpZli8aPFSrto4gbtHNSeZIbSpu5GqxiQ_j8xV46YO2DXZCLHUFtNlYLRE0xuK_7mJIilCYLKniA8lNtj1yb6WWcqmRLUF0SJrpo8q584RZfUPOrYDbzAfS4BRu_PlLhUJK82OT-n8xhwXqblL7lz499d58xObYeTKL825MrNka-8WO4XU95yFgZkcKGgxorzW3iy4FR0W1AbHj4nu0mswp7sUkZIlrq9KnFkUQTdctSbmi-FVC2mAGsz58amUoX9OpOCRC5sM8r00wZex8oAZoAXPYAHsDbIVSEP6f8rgJfBUGev7MNPC2HJZVsemrMkVTH3BOqw",
    'cache-control': "no-cache",
    'Postman-Token': "71a3e047-3d9c-4f93-bec4-858bf59ee9fa"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring).json()

print(response)

ta_info = response['campaigns'] 
   
if os.path.exists("ta_logs.csv"):
  os.remove("ta_logs.csv")
  
ta_file = open('ta_logs.csv', 'x')

csvwriter = csv.writer(ta_file)

count = 0

for log in ta_info:

      if count == 0:

             header = log.keys()

             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(log.values())
      
ta_file.close()

with open('ta_logs.csv','r') as total:
    reader = csv.reader(total,delimiter = "\n")
    data = list(reader)
    row_count = len(data) - 1
    final_row = str(row_count)


print("You have " + final_row + " warnings for TripAdvisors S2S")
print("TUNA API Script Complete!")
p = Popen('ta_logs.csv', shell=True)
