# encoding=utf-8
import json


data = {
    "errcode": 0,
    "errmsg": "ok",
    "process_instance": {
        "attached_process_instance_ids": [],
        "biz_action": "NONE",
        "business_id": "202205302346000370844",
        "cc_userids": [
            "14256020681178090",
            "0161240911691516",
            "192029451824282523",
            "1303095609748656"
        ],
        "create_time": "2022-05-30 23:46:37",
        "finish_time": "2022-05-31 09:54:40",
        "form_component_values": [
            {
                "component_type": "DDSelectField",
                "ext_value": "{\"label\":\"出差\",\"key\":\"option_0\"}",
                "id": "DDSelectField_1XO0NHHZ6KJK0",
                "name": "出勤状态",
                "value": "出差"
            },
            {
                "component_type": "TextField",
                "id": "TextField_W5G7KPJ38EO0",
                "name": "上班时间",
                "value": "9：00"
            },
            {
                "component_type": "TextField",
                "id": "TextField_WNY7YCK27KW0",
                "name": "下班时间",
                "value": "19：00"
            },
            {
                "component_type": "DDMultiSelectField",
                "ext_value": "[{\"label\":\"无\",\"key\":\"option_0\"}]",
                "id": "DDMultiSelectField_1U1JMGYQVDZ40",
                "name": "上班期间中途是否外出",
                "value": "[\"无\"]"
            },
            {
                "component_type": "DDSelectField",
                "ext_value": "{\"label\":\"实施\",\"key\":\"option_0\"}",
                "id": "DDSelectField_21QCA2NPLJKW0",
                "name": "工作内容",
                "value": "实施"
            },
            {
                "component_type": "DDDateField",
                "id": "DDDateField_ITHUFEYY8BK0",
                "name": "日志日期",
                "value": "2022-05-30"
            },
            {
                "component_type": "TextField",
                "id": "TextField-K2AD4O5B",
                "name": "项目编号",
                "value": "A51376"
            },
            {
                "component_type": "TextField",
                "id": "TextField_FSPC9O46F080",
                "name": "项目名称",
                "value": "上海维自杭州阅布纺织仓储项目"
            },
            {
                "component_type": "InnerContactField",
                "ext_value": "[{\"emplId\":\"205937523932471911\",\"name\":\"肖有为\",\"selectDeptName\":\"\",\"avatar\":\"https://static.dingtalk.com/media/lADPDhmOylYHUfrNAoDNAoA_640_640.jpg_120x120q90.jpg?bizType=avatar\",\"selectDeptId\":\"\"}]",
                "id": "InnerContactField_1R9B45BYVYE80",
                "name": "项目经理",
                "value": "肖有为"
            },
            {
                "component_type": "TextField",
                "id": "TextField_UJ4NUA5NVWW0",
                "name": "现场团队成员",
                "value": "储向濮"
            },
            {
                "component_type": "TableField",
                "ext_value": "{\"statValue\":[],\"componentName\":\"TableField\"}",
                "id": "TableField_1BDACPXDIFEO0",
                "name": "当日任务统计",
                "value": "[{\"rowValue\":[{\"componentType\":\"DDSelectField\",\"label\":\"是否为项目现场第一次正式实施（不包括演示）\",\"extendValue\":{\"label\":\"是\",\"key\":\"option_0\"},\"value\":\"是\",\"key\":\"DDSelectField_6H05X8C9MQW0\"},{\"componentType\":\"DDSelectField\",\"label\":\"任务类型\",\"extendValue\":{\"extension\":{\"image\":\"\"},\"label\":\"实施内部验证\",\"key\":\"option_576LHS7QBV40\"},\"value\":\"实施内部验证\",\"key\":\"DDSelectField_13PG9B1A8TY80\"},{\"componentType\":\"NumberField\",\"label\":\"工作时长（小时）\",\"value\":\"10\",\"key\":\"NumberField_CJLLRN312VS0\"},{\"componentType\":\"DDSelectField\",\"label\":\"劳务人数\",\"extendValue\":{\"label\":\"无\",\"key\":\"option_0\"},\"value\":\"无\",\"key\":\"DDSelectField_2VD9KVNTQHO0\"},{\"componentType\":\"DDSelectField\",\"label\":\"任务状态\",\"extendValue\":{\"label\":\"进行中\",\"key\":\"option_0\"},\"value\":\"进行中\",\"key\":\"DDSelectField_J4CXZR98TE00\"}],\"rowNumber\":\"TableField_1BDACPXDIFEO0_217YI4EVSTI80\"}]"
            },
            {
                "component_type": "TextareaField",
                "id": "TextareaField_1R5QTEF2J2SG0",
                "name": "公司办公工作内容",
                "value": "null"
            },
            {
                "component_type": "TextareaField",
                "id": "TextareaField_MRHZX8GK27K0",
                "name": "明日计划安排",
                "value": "1.联调测试"
            },
            {
                "component_type": "TextareaField",
                "id": "TextareaField_PL63NZ0E3740",
                "name": "今日完成",
                "value": "1.路径测试"
            },
            {
                "component_type": "TextareaField",
                "id": "TextareaField_1K334ML768QO0",
                "name": "是否有逾期or逾期风险",
                "value": "否"
            },
            {
                "component_type": "DDAttachment",
                "id": "DDAttachment_D37VXHQUCG00",
                "name": "附件（Axxxxx-ISL-问题日志-YYMMDD）",
                "value": "[{\"spaceId\":\"115770306\",\"fileName\":\"A51376  上海维自杭州阅布项目  过程管控文档(13).xlsx\",\"fileSize\":267266,\"fileType\":\"xlsx\",\"fileId\":\"60605779562\"}]"
            },
            {
                "component_type": "TableField",
                "id": "TableField_K404KZ5IATS0",
                "name": "故障统计",
                "value": "[{\"componentName\":\"TextField\",\"componentType\":\"TextField\",\"props\":{\"bizAlias\":\"\",\"holidayOptions\":[],\"id\":\"TextField_ONWDW0U26YO0\",\"label\":\"故障类型\",\"placeholder\":\"请输入\",\"required\":true}},{\"componentName\":\"TextField\",\"componentType\":\"TextField\",\"props\":{\"bizAlias\":\"\",\"holidayOptions\":[],\"id\":\"TextField_MNZ9W6GQ0800\",\"label\":\"故障数量\",\"placeholder\":\"请输入\",\"required\":true}},{\"componentName\":\"TextField\",\"componentType\":\"TextField\",\"props\":{\"bizAlias\":\"\",\"holidayOptions\":[],\"id\":\"TextField_16OQSYRTVQQO0\",\"label\":\"重要问题处理计划\",\"placeholder\":\"请输入\",\"required\":true}}]"
            },
            {
                "component_type": "TextField",
                "id": "TextField_ML561AHB7GW0",
                "name": "故障数量统计",
                "value": "null"
            },
            {
                "component_type": "DDSelectField",
                "id": "DDSelectField_14HQYTJIZ6V40",
                "name": "是否7*24h工作",
                "value": "null"
            },
            {
                "component_type": "NumberField",
                "id": "NumberField_OOAGS5RL2OG0",
                "name": "搬运任务数量",
                "value": "null"
            },
            {
                "component_type": "TextareaField",
                "id": "TextareaField_HOWCDKV4UK80",
                "name": "备注",
                "value": "null"
            }
        ],
        "operation_records": [
            {
                "date": "2022-05-30 23:46:37",
                "operation_result": "NONE",
                "operation_type": "START_PROCESS_INSTANCE",
                "userid": "214648015520538533"
            },
            {
                "date": "2022-05-30 23:46:37",
                "operation_result": "NONE",
                "operation_type": "PROCESS_CC",
                "remark": "",
                "userid": "214648015520538533"
            },
            {
                "date": "2022-05-31 09:54:39",
                "operation_result": "AGREE",
                "operation_type": "EXECUTE_TASK_NORMAL",
                "remark": "",
                "userid": "205937523932471911"
            },
            {
                "date": "2022-05-31 09:54:40",
                "operation_result": "NONE",
                "operation_type": "PROCESS_CC",
                "remark": "",
                "userid": "214648015520538533"
            }
        ],
        "originator_dept_id": "582976341",
        "originator_dept_name": "营销中心-华东大区-项目交付组-PE-二组",
        "originator_userid": "214648015520538533",
        "result": "agree",
        "status": "COMPLETED",
        "tasks": [
            {
                "activity_id": "b39a_73fb",
                "create_time": "2022-05-30 23:46:38",
                "finish_time": "2022-05-31 09:54:40",
                "task_result": "AGREE",
                "task_status": "COMPLETED",
                "taskid": "74296847418",
                "url": "aflow.dingtalk.com?procInsId=oyTxr2qkQXqjgjJNZZATZQ00891653925597&taskId=74296847418&businessId=202205302346000370844",
                "userid": "205937523932471911"
            }
        ],
        "title": "储向濮提交的PE日志"
    },
    "request_id": "16m5y0pwzks9t"
}
process_instance = data.get('process_instance')
print(process_instance)
form_component = process_instance.get('form_component_values')
TableField = form_component[10].get('value')
tab = json.loads(TableField)
tab1 = tab[0]
print(tab1)
ac = tab1.get('rowValue')

if ac is None:
    ac = tab
    props = tab[0].get('props')
    First = props.get('placeholder')

    props1 = tab[1].get('props')
    tasks = props1.get('placeholder')

    props2 = tab[2].get('props')
    Working = props2.get('placeholder')

    props3 = tab[3].get('props')
    employees = props3.get('placeholder')

    props4 = tab[4].get('props')
    status = props4.get('placeholder')

    props5 = tab[5].get('props')
    Note = props5.get('placeholder')
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

print(First)
print(tasks)
print(Working)
print(employees)
print(status)
print(Note)