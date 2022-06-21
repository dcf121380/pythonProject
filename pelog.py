# encoding=utf-8

import datetime
import json
import time
from urllib import request, parse

import pymysql
import requests
import schedule


# 引入schedule和time

def get_access_token():
    try:
        appkey = "dingdjzudqpvrqlucocs"
        appsecret = "jsAmLunzCW0kUdt46fSEkS_cM9LEcad_kJpoBPdS2sJCa1jJd3ruKvB_KGrYsuZS"
        textmod = {"grant_type": "client_credential",
                   "appkey": appkey,
                   "appsecret": appsecret
                   }
        textmod = parse.urlencode(textmod)
        header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
        accesstoken_url = 'https://oapi.dingtalk.com/gettoken'
        req = request.Request(url='%s%s%s' % (accesstoken_url, '?', textmod), headers=header_dict)
        res = request.urlopen(req)
        res = res.read().decode(encoding='utf-8')
        res = json.loads(res)
        access_token = res["access_token"]
        return access_token
    except Exception as e:
        print(e)
        return False


'''
today = datetime.date.today()
print(today)
# 昨天时间
yesterday = today - datetime.timedelta(days=1)
star = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')) + 36000)

start_time = str(star * 1000)
end_time = str((star + 86400 - 1) * 1000)'''

start_time = "1655652077000"
end_time = "1655652077000"
process_code = "PROC-C6C11B47-A8C4-441E-B8AF-974ECA6ED476"
size = str(20)
cursor = ['{0}'.format(i) for i in range(1, 1 + 1)]
access_token = get_access_token()
for next_cursor in cursor:
    print(next_cursor)
    url = 'https://oapi.dingtalk.com/topapi/processinstance/listids?access_token=' + access_token + '&process_code=' + process_code + '&start_time=' + start_time + '&size=' + size + '&cursor=' + next_cursor + '&end_time=' + end_time + ''


    def get_page(url):
        # requests.get 自带 json.load
        page = requests.get(url)
        page = page.content
        # 将bytes转换成字符串
        page = page.decode('utf-8')
        return page


    li = json.loads(get_page(url))
    result = li.get('result')
    process = result.get('list')
    for process_id in process:
        list = [get_page(
            'https://oapi.dingtalk.com/topapi/processinstance/get?access_token=' + access_token + '&process_instance_id=' + process_id + '')]
        print(process_id)
        print(list)
        for data in list:
            data = json.loads(data)
            process_instance = data.get("process_instance")
            form_component_values = process_instance.get("form_component_values")
            title = process_instance.get('title')
            TableField = form_component_values[10].get('value')
            tab = json.loads(TableField)
            tab1 = tab[0]
            ac = tab1.get('rowValue')
            if ac is None:
                ac = tab
                First = 'null'

                tasks = 'null'

                Working = 'null'

                employees = 'null'

                status = 'null'

                Note = 'null'
            else:
                ac = tab1.get('rowValue')[0]
                First = ac.get('value')

                ac1 = tab1.get('rowValue')[1]
                tasks = ac1.get('value')

                ac2 = tab1.get('rowValue')[2]
                Working = ac2.get('value')

                ac3 = tab1.get('rowValue')[3]
                employees = ac3.get('value')

                ac4 = tab1.get('rowValue')[4]
                status = ac4.get('value')

                ac5 = tab1.get('rowValue')
                if 5 in ac5:
                    Note = ac4.get('value')
                else:
                    Note = 'null'

            statValue = form_component_values[16].get('value')
            tab2 = json.loads(statValue)
            season = tab2
            Fault = []
            others = []
            failures = []
            resolution = []
            for i, element in enumerate(season):
                tab3 = tab2[i]
                ad = tab3.get('rowValue')
                if ad is None:
                    ad = tab2
                    Fault = 'null'

                    others = 'null'

                    failures = 'null'

                    resolution = 'null'

                else:
                    ad = tab3.get('rowValue')[0]
                    Faults = ad.get('value')
                    Fault.append(Faults)

                    if Faults == "其他  others":
                        ad1 = tab3.get('rowValue')[1]
                        other = ad1.get('value')

                        ad2 = tab3.get('rowValue')[2]
                        failure = ad2.get('value')

                        ad3 = tab3.get('rowValue')[3]
                        resolutions = ad3.get('value')

                    else:
                        other = 'null'

                        ad2 = tab3.get('rowValue')[1]
                        failure = ad2.get('value')

                        ad3 = tab3.get('rowValue')[2]
                        resolutions = ad3.get('value')
                    others.append(other)
                    failures.append(failure)
                    resolution.append(resolutions)

        dtp = {
            "business_id": process_instance.get("business_id"),
            "create_time": process_instance.get("create_time"),
            "originator_dept_id": process_instance.get("originator_dept_id"),
            "originator_dept_name": process_instance.get("originator_dept_name"),
            "originator_userid": process_instance.get("originator_userid"),
            "founder": title.strip('提交的PE日志(PE daily report)'),
            "Attendance_status": form_component_values[0].get("value"),
            "Attendance_time": form_component_values[1].get("value"),
            "Off_work_time": form_component_values[2].get("value"),
            "egress": form_component_values[3].get("value"),
            "Job_content": form_component_values[4].get("value"),
            "Report_date": form_component_values[5].get("value"),
            "Project_NO": form_component_values[6].get("value"),
            "Project_name": form_component_values[7].get("value"),
            "PM": form_component_values[8].get("value"),
            "site_personnel": form_component_values[9].get("value"),
            "First_time_implement": First,
            "Types_of_tasks": tasks,
            "Working_hours": Working,
            "Number_of_employees": employees,
            "Task_status": status,
            "Note": Note,
            "work_company": form_component_values[11].get("value"),
            "Tomorrow_Plan": form_component_values[12].get("value"),
            "Today_Completed": form_component_values[13].get("value"),
            "Overdue_risk": form_component_values[14].get("value"),
            "Fault_type": str(Fault),
            "others": str(others),
            "Number_of_failures": str(failures),
            "Problem_resolution_plan": str(resolution),
            "Fault_statistics": form_component_values[17].get("value"),
            "works_7_24h": form_component_values[18].get("value"),
            "carry_number": form_component_values[19].get("value"),
            "remarks": form_component_values[20].get("value")
        }
        print(dtp)

        conn = pymysql.connect(host='localhost', user='root', password='root', db='work2022', port=3306,
                               charset='utf8')
        print('连接数据库成功！')
        cursor = conn.cursor()
        table = 'pelog'
        keys = ', '.join(dtp.keys())
        values = ', '.join(['%s'] * len(dtp))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        try:
            cursor.execute(sql, tuple(dtp.values()))
            print('Successful')
            conn.commit()
        except:
            print('Failed')
            conn.rollback()
        cursor.close()
        conn.close()
