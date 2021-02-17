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