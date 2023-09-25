import requests
import json
import string

#connection string
response = requests.get("https://cat-fact.herokuapp.com/facts/")

#json reader
fact_dict = response.json()
fact_str = json.dumps(fact_dict)
fact_dict = json.loads(fact_str)
#print(fact_dict)

#file reader
for idx, fact_dict in enumerate(fact_dict, start=1):
    print(f"Cat Fact {idx}:")
    print("Text:", fact_dict['text'])
    print("Type:", fact_dict['type'])
    print("Verified:", fact_dict['status']['verified'])
    print("Used:", fact_dict['used'])
    print("Source:", fact_dict['source'])
    print("Created At:", fact_dict['createdAt'])
    print("Updated At:", fact_dict['updatedAt'])
