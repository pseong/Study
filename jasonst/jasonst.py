import json

data = {
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
            "List2": ["Mylist1", "Mylist2"]
        }
    ]
} 

with open("jasonst.json", "w") as json_file:
    json.dump(data, json_file)
# jason 파일로 출력

jason_str = json.dumps(data) # 한줄로 생성
print(jason_str)
jason_str3 = json.dumps(data, sort_keys=True) # 정렬
print(jason_str3)
jason_str2 = json.dumps(data, indent=4) # indent만큼 들여쓰기
print(jason_str2)

