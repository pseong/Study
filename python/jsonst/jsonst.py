import json

data_dic = {
    "Name": "SeongUk",
    "Age": 23, 
    "List": [
        {
            "Name": "SeongUk2", 
            "Age": 23
        }, 
        {
            "Name": "SeongUk3",
            "Age": 23,
            "List2": ["MyList1", "MyList2"]
        }
    ],
    "false": False,
    "null": None
}

data_str = '''{
    "Name": "SeongUk",
    "Age": 23, 
    "List": [
        {
            "Name": "SeongUk2", 
            "Age": 23
        }, 
        {
            "Name": "SeongUk3",
            "Age": 23,
            "List2": ["MyList1", "MyList2"]
        }
    ],
    "false": false,
    "null": null
}'''

with open("jsonst.json", "w") as json_file_w:
    json.dump(data_dic, json_file_w)
# jason 파일로 출력

json_str1 = json.dumps(data_dic)
# 한줄로 생성
json_str2 = json.dumps(data_dic, sort_keys=True)
# 정렬
json_str3 = json.dumps(data_dic, indent=4)
# indent만큼 들여쓰기

with open("jsonst.json", "r") as json_file_r:
    json_dic = json.load(json_file_r)
# jason 파일 입력

json_dic2 = json.loads(data_str)
# jason 파일 입력2