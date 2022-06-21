# encoding=utf-8
import json


data = {
    "errcode": 0,
    "errmsg": "ok",
    "process_instance": {
        "attached_process_instance_ids": [],
        "biz_action": "NONE",
        "business_id": "202206192321000178717",
        "cc_userids": [
            "102719593020960182",
            "0704393456653664",
            "14256020681178090"
        ],
        "create_time": "2022-06-19 23:21:17",
        "finish_time": "2022-06-19 23:25:09",
        "form_component_values": [
            {
                "component_type": "DDSelectField",
                "ext_value": "{\"label\":\"出差/On business trip\",\"key\":\"option_0\"}",
                "id": "DDSelectField_1XO0NHHZ6KJK0",
                "name": "出勤状态/Attendance status",
                "value": "出差/On business trip"
            },
            {
                "component_type": "DDDateField",
                "id": "DDDateField_1GDK7Q57ZTK00",
                "name": "上班时间/Attendance time",
                "value": "2022-06-19 07:30"
            },
            {
                "component_type": "DDDateField",
                "id": "DDDateField_1AYXIKU6VEHS0",
                "name": "下班时间/Off work time",
                "value": "2022-06-19 20:30"
            },
            {
                "component_type": "DDMultiSelectField",
                "ext_value": "[{\"label\":\"无/NO\",\"key\":\"option_1ES9ZFX6WO3K0\"}]",
                "id": "DDMultiSelectField_1U1JMGYQVDZ40",
                "name": "上班中途是否外出/Do you go off from site during work time？",
                "value": "[\"无/NO\"]"
            },
            {
                "component_type": "DDSelectField",
                "ext_value": "{\"label\":\"运维/Operational Running\",\"key\":\"option_1\"}",
                "id": "DDSelectField_21QCA2NPLJKW0",
                "name": "工作内容/Job content",
                "value": "运维/Operational Running"
            },
            {
                "component_type": "DDDateField",
                "id": "DDDateField_ITHUFEYY8BK0",
                "name": "日志日期/Report date",
                "value": "2022-06-19"
            },
            {
                "component_type": "TextField",
                "id": "TextField-K2AD4O5B",
                "name": "项目编号/Project NO.",
                "value": "FH-B2021-C100"
            },
            {
                "component_type": "TextField",
                "id": "TextField_FSPC9O46F080",
                "name": "项目名称/Project name",
                "value": "利丰POC维密项目"
            },
            {
                "component_type": "InnerContactField",
                "ext_value": "[{\"emplId\":\"203562535620041938\",\"name\":\"乔巧梅\",\"selectDeptName\":\"\",\"avatar\":\"https://static.dingtalk.com/media/lADPDgQ9rBrY6SjNChDNB4w_1932_2576.jpg_120x120q90.jpg?bizType=avatar\",\"selectDeptId\":\"\"}]",
                "id": "InnerContactField_1R9B45BYVYE80",
                "name": "项目经理/PM",
                "value": "乔巧梅"
            },
            {
                "component_type": "TextField",
                "id": "TextField_UJ4NUA5NVWW0",
                "name": "现场团队成员/Team members on site",
                "value": "唐威亮 钟红洋 常振翔"
            },
            {
                "component_type": "TableField",
                "id": "TableField_1BDACPXDIFEO0",
                "name": "当日任务统计/Daily task statistics",
                "value": "[{\"componentName\":\"DDSelectField\",\"componentType\":\"DDSelectField\",\"props\":{\"behaviorLinkage\":[],\"bizAlias\":\"\",\"fields\":[],\"fieldsInfo\":\"[]\",\"holidayOptions\":[],\"id\":\"DDSelectField_6H05X8C9MQW0\",\"label\":\"是否为项目现场第一次正式实施（不包括演示)/First time to implement in s\",\"options\":[\"{\\\"value\\\":\\\"是/Yes\\\",\\\"key\\\":\\\"option_0\\\"}\",\"{\\\"value\\\":\\\"否/No\\\",\\\"key\\\":\\\"option_1\\\"}\"],\"placeholder\":\"请选择\",\"required\":true}},{\"componentName\":\"DDSelectField\",\"componentType\":\"DDSelectField\",\"props\":{\"behaviorLinkage\":[],\"bizAlias\":\"\",\"fields\":[],\"fieldsInfo\":\"[]\",\"holidayOptions\":[],\"id\":\"DDSelectField_13PG9B1A8TY80\",\"label\":\"任务类型/Types of tasks\",\"options\":[\"{\\\"value\\\":\\\"现场环境检测/Environmental detection\\\",\\\"key\\\":\\\"option_9L8BHN1FALK\\\"}\",\"{\\\"value\\\":\\\"服务器检测和部署/Server detection and deployment\\\",\\\"key\\\":\\\"option_1SLFVUZ59G680\\\"}\",\"{\\\"value\\\":\\\"现场网络检测和配置/Network check and configuration\\\",\\\"key\\\":\\\"option_2\\\"}\",\"{\\\"value\\\":\\\"划线贴码/Lineation and post code\\\",\\\"key\\\":\\\"option_K3TP2AG4MC0\\\"}\",\"{\\\"value\\\":\\\"货架组装/Assemble rack\\\",\\\"key\\\":\\\"option_ZY6IVFUJUY80\\\"}\",\"{\\\"value\\\":\\\"充电桩安装/Install charger\\\",\\\"key\\\":\\\"option_HTVQU2YBAU80\\\"}\",\"{\\\"value\\\":\\\"工作站安装/Install workstation\\\",\\\"key\\\":\\\"option_1HF1YIPXPVY80\\\"}\",\"{\\\"value\\\":\\\"货架归位/Rack place\\\",\\\"key\\\":\\\"option_11MU28DG2CHC0\\\"}\",\"{\\\"value\\\":\\\"安装网络设备和系统部署/Install network devices and deploy the system\\\",\\\"key\\\":\\\"option_LL1XNQO78VK0\\\"}\",\"{\\\"value\\\":\\\"开仓/System data initialization\\\",\\\"key\\\":\\\"option_11YCOZCDUD800\\\"}\",\"{\\\"value\\\":\\\"AGV上线/online\\\",\\\"key\\\":\\\"option_VJB8QDLMG6O0\\\"}\",\"{\\\"value\\\":\\\"货架验证/Verify the rack\\\",\\\"key\\\":\\\"option_1W3T0Q5KT1MO0\\\"}\",\"{\\\"value\\\":\\\"货位验证/Verify the place\\\",\\\"key\\\":\\\"option_10UBKOYJFVCG0\\\"}\",\"{\\\"value\\\":\\\"实施内部验证/Internal validation\\\",\\\"key\\\":\\\"option_576LHS7QBV40\\\"}\",\"{\\\"value\\\":\\\"接口联调/Commissioning tests\\\",\\\"key\\\":\\\"option_1YFERP50NISG0\\\"}\",\"{\\\"value\\\":\\\"修车/Repair of AGV\\\",\\\"key\\\":\\\"option_TOTKZ3CAH9C0\\\"}\",\"{\\\"value\\\":\\\"培训/Training\\\",\\\"key\\\":\\\"option_T9C6EKD1D9C0\\\"}\",\"{\\\"value\\\":\\\"陪产/Production Support\\\",\\\"key\\\":\\\"option_1JMEZNP6RE9S0\\\"}\",\"{\\\"value\\\":\\\"UAT测试/UAT\\\",\\\"key\\\":\\\"option_1SPT175TR5400\\\"}\",\"{\\\"value\\\":\\\"其他/Etc\\\",\\\"key\\\":\\\"option_PHNH6CKDM2O0\\\"}\"],\"placeholder\":\"请选择\",\"required\":true}},{\"componentName\":\"NumberField\",\"componentType\":\"NumberField\",\"props\":{\"bizAlias\":\"\",\"holidayOptions\":[],\"id\":\"NumberField_CJLLRN312VS0\",\"label\":\"工作时长（小时）/Working hours\",\"placeholder\":\"请输入数字\",\"required\":true}},{\"componentName\":\"DDSelectField\",\"componentType\":\"DDSelectField\",\"props\":{\"behaviorLinkage\":[],\"bizAlias\":\"\",\"fields\":[],\"fieldsInfo\":\"[]\",\"holidayOptions\":[],\"id\":\"DDSelectField_2VD9KVNTQHO0\",\"label\":\"劳务人数/Number of employees\",\"options\":[\"{\\\"value\\\":\\\"无\\\",\\\"key\\\":\\\"option_0\\\"}\",\"{\\\"value\\\":\\\"1\\\",\\\"key\\\":\\\"option_1\\\"}\",\"{\\\"value\\\":\\\"2\\\",\\\"key\\\":\\\"option_2\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"3\\\",\\\"key\\\":\\\"option_1VRRVKMKEAAO0\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"4\\\",\\\"key\\\":\\\"option_123CL5MIQ1Q80\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"5\\\",\\\"key\\\":\\\"option_1H971RHSB0HS0\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"6\\\",\\\"key\\\":\\\"option_21CAKGV1YMM80\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"7\\\",\\\"key\\\":\\\"option_AQONRCARBQ80\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"8\\\",\\\"key\\\":\\\"option_7VLY1ECG6LC0\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"9\\\",\\\"key\\\":\\\"option_EGM5ACT6L8O0\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"10\\\",\\\"key\\\":\\\"option_200JL0U8ONTS0\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"11\\\",\\\"key\\\":\\\"option_1DW4XM2TIKXS0\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"12\\\",\\\"key\\\":\\\"option_210P2X7YE7I80\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"13\\\",\\\"key\\\":\\\"option_1QK4CYRR160W0\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"14\\\",\\\"key\\\":\\\"option_2INSVUB7FZ20\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"15\\\",\\\"key\\\":\\\"option_21NTEB1V6AG00\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"16\\\",\\\"key\\\":\\\"option_1PUSL070QBKW0\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"17\\\",\\\"key\\\":\\\"option_10ZHKMYSXDC00\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"18\\\",\\\"key\\\":\\\"option_VY4PXTZTFSW0\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"19\\\",\\\"key\\\":\\\"option_HYPQBSW6KJ40\\\"}\",\"{\\\"extension\\\":{\\\"image\\\":\\\"\\\"},\\\"value\\\":\\\"20\\\",\\\"key\\\":\\\"option_16RPXLKG3AF40\\\"}\"],\"placeholder\":\"请选择\",\"required\":true}},{\"componentName\":\"DDSelectField\",\"componentType\":\"DDSelectField\",\"props\":{\"behaviorLinkage\":[],\"bizAlias\":\"\",\"fields\":[],\"fieldsInfo\":\"[]\",\"holidayOptions\":[],\"id\":\"DDSelectField_J4CXZR98TE00\",\"label\":\"任务状态/Task status\",\"options\":[\"{\\\"value\\\":\\\"进行中/In progress\\\",\\\"key\\\":\\\"option_0\\\"}\",\"{\\\"value\\\":\\\"已完成/Completed\\\",\\\"key\\\":\\\"option_1\\\"}\"],\"placeholder\":\"请选择\",\"required\":true}},{\"componentName\":\"TextareaField\",\"componentType\":\"TextareaField\",\"props\":{\"bizAlias\":\"\",\"holidayOptions\":[],\"id\":\"TextareaField_1KBOI35XI3GG0\",\"label\":\"备注/Note\",\"placeholder\":\"请输入\",\"required\":false}}]"
            },
            {
                "component_type": "TextareaField",
                "id": "TextareaField_1R5QTEF2J2SG0",
                "name": "公司办公工作内容/work of the company",
                "value": "null"
            },
            {
                "component_type": "TextareaField",
                "id": "TextareaField_MRHZX8GK27K0",
                "name": "明日计划安排/Tomorrow Plan",
                "value": "null"
            },
            {
                "component_type": "TextareaField",
                "id": "TextareaField_PL63NZ0E3740",
                "name": "今日完成/Completed",
                "value": "null"
            },
            {
                "component_type": "TextareaField",
                "id": "TextareaField_1K334ML768QO0",
                "name": "是否有逾期or逾期风险/Overdue or risk",
                "value": "null"
            },
            {
                "component_type": "DDAttachment",
                "id": "DDAttachment_D37VXHQUCG00",
                "name": "附件（Axxxxx-ISL-问题日志-YYMMDD）/Issues list-YYMMDD",
                "value": "[{\"spaceId\":\"115770306\",\"fileName\":\"FH-B2021-C100利丰维密项目现场故障统计(1)_54949_1003.xlsx\",\"fileSize\":4028863,\"fileType\":\"xlsx\",\"fileId\":\"62086316315\"},{\"spaceId\":\"115770306\",\"fileName\":\"FH-B2021-C100上海利丰项目问题日志（运行） (10).xls\",\"fileSize\":7858688,\"fileType\":\"xls\",\"fileId\":\"62086384339\"}]"
            },
            {
                "component_type": "TableField",
                "ext_value": "{\"statValue\":[],\"componentName\":\"TableField\"}",
                "id": "TableField_K404KZ5IATS0",
                "name": "故障统计",
                "value": "[{\"rowValue\":[{\"componentType\":\"DDSelectField\",\"label\":\"故障类型/Fault type\",\"extendValue\":{\"label\":\"其他  others\",\"key\":\"option_1W0IKGHUNPLS0\"},\"value\":\"其他  others\",\"key\":\"DDSelectField_1IGEL0DUOFZ40\"},{\"componentType\":\"TextField\",\"label\":\"其他问题/others\",\"value\":\"73\",\"key\":\"TextField_5HM8JU8VU0W0\"},{\"componentType\":\"TextField\",\"label\":\"故障数量/Number of failures\",\"value\":\"1\",\"key\":\"TextField_MNZ9W6GQ0800\"},{\"componentType\":\"TextField\",\"label\":\"重要问题处理计划/Problem resolution plan\",\"value\":\"手动清错恢复\",\"key\":\"TextField_16OQSYRTVQQO0\"}],\"rowNumber\":\"TableField_K404KZ5IATS0_1JP5JWYD2DZ40\"},{\"rowValue\":[{\"componentType\":\"DDSelectField\",\"label\":\"故障类型/Fault type\",\"extendValue\":{\"label\":\"其他  others\",\"key\":\"option_1W0IKGHUNPLS0\"},\"value\":\"其他  others\",\"key\":\"DDSelectField_1IGEL0DUOFZ40\"},{\"componentType\":\"TextField\",\"label\":\"其他问题/others\",\"value\":\"78\",\"key\":\"TextField_5HM8JU8VU0W0\"},{\"componentType\":\"TextField\",\"label\":\"故障数量/Number of failures\",\"value\":\"1\",\"key\":\"TextField_MNZ9W6GQ0800\"},{\"componentType\":\"TextField\",\"label\":\"重要问题处理计划/Problem resolution plan\",\"value\":\"测试缓存位\",\"key\":\"TextField_16OQSYRTVQQO0\"}],\"rowNumber\":\"TableField_K404KZ5IATS0_41CZFM2PVYC0\"},{\"rowValue\":[{\"componentType\":\"DDSelectField\",\"label\":\"故障类型/Fault type\",\"extendValue\":{\"label\":\"其他  others\",\"key\":\"option_1W0IKGHUNPLS0\"},\"value\":\"其他  others\",\"key\":\"DDSelectField_1IGEL0DUOFZ40\"},{\"componentType\":\"TextField\",\"label\":\"其他问题/others\",\"value\":\"29\",\"key\":\"TextField_5HM8JU8VU0W0\"},{\"componentType\":\"TextField\",\"label\":\"故障数量/Number of failures\",\"value\":\"1\",\"key\":\"TextField_MNZ9W6GQ0800\"},{\"componentType\":\"TextField\",\"label\":\"重要问题处理计划/Problem resolution plan\",\"value\":\"手动清错恢复\",\"key\":\"TextField_16OQSYRTVQQO0\"}],\"rowNumber\":\"TableField_K404KZ5IATS0_118T8JMPEW1S0\"}]"
            },
            {
                "component_type": "TextField",
                "id": "TextField_ML561AHB7GW0",
                "name": "故障数量统计/Fault statistics",
                "value": "3"
            },
            {
                "component_type": "DDSelectField",
                "ext_value": "{\"label\":\"否\",\"key\":\"option_1\"}",
                "id": "DDSelectField_14HQYTJIZ6V40",
                "name": "是否7*24h工作/Whether to work 24*7",
                "value": "否"
            },
            {
                "component_type": "NumberField",
                "id": "NumberField_OOAGS5RL2OG0",
                "name": "搬运任务数量/Number of carry task",
                "value": "6786"
            },
            {
                "component_type": "TextareaField",
                "id": "TextareaField_HOWCDKV4UK80",
                "name": "备注/Note",
                "value": "null"
            }
        ],
        "operation_records": [
            {
                "date": "2022-06-19 23:21:17",
                "operation_result": "NONE",
                "operation_type": "START_PROCESS_INSTANCE",
                "userid": "523751021721661149"
            },
            {
                "date": "2022-06-19 23:21:17",
                "operation_result": "NONE",
                "operation_type": "PROCESS_CC",
                "remark": "",
                "userid": "523751021721661149"
            },
            {
                "date": "2022-06-19 23:21:17",
                "operation_result": "NONE",
                "operation_type": "PROCESS_CC",
                "remark": "",
                "userid": "523751021721661149"
            },
            {
                "date": "2022-06-19 23:25:08",
                "operation_result": "AGREE",
                "operation_type": "EXECUTE_TASK_NORMAL",
                "remark": "",
                "userid": "203562535620041938"
            },
            {
                "date": "2022-06-19 23:25:08",
                "operation_result": "NONE",
                "operation_type": "PROCESS_CC",
                "remark": "",
                "userid": "523751021721661149"
            }
        ],
        "originator_dept_id": "575403278",
        "originator_dept_name": "项目部-项目交付组-实施运维组-五组",
        "originator_userid": "523751021721661149",
        "result": "agree",
        "status": "COMPLETED",
        "tasks": [
            {
                "activity_id": "b39a_73fb",
                "create_time": "2022-06-19 23:21:18",
                "finish_time": "2022-06-19 23:25:09",
                "task_result": "AGREE",
                "task_status": "COMPLETED",
                "taskid": "74521025574",
                "url": "aflow.dingtalk.com?procInsId=F9fLKNnORp2TZ90JyxE0vw00891655652077&taskId=74521025574&businessId=202206192321000178717",
                "userid": "203562535620041938"
            }
        ],
        "title": "唐威亮提交的PE日志(PE daily report)"
    },
    "request_id": "16lu6e15l9flz"
}
process_instance = data.get('process_instance')
print(process_instance)
form_component = process_instance.get('form_component_values')
statValue = form_component[16].get('value')
print(statValue)
tab2 = json.loads(statValue)
print(tab2)
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
print(Fault)
print(others)
print(failures)
print(resolution)






