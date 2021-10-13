# imports, both are built-in modules
import json
import random


# will add whatever dictionary is provided to a JSON file in an array
def log_to_json(dict):
    with open("logs.json", mode='r', encoding='utf-8') as f:
            feeds = json.load(f)
            
    with open("logs.json", mode='w', encoding='utf-8') as feedsjson:
        entry = dict
        feeds.append(entry)        
        json.dump(feeds, feedsjson, indent=2)

        
# function to parse the data we created by searching for the 'message_id' provided and returning to python as a dictionary
# message_id is the key value of the json log
def parse_from_json(message_id):
    f = open("logs.json", mode='r', encoding='utf-8')
    data_list = json.load(f)
    index = 0
    while index < len(data_list):
        if data_list[index]["log_id"] == message_id:
            return data_list[index]
        index += 1



# this just makes random entries for me to demonstrate with
int = random.randint(0, 100000000)
new_item = {"log_id": int,
            "data": {
                "Discord User": "Test " + str(int),
                "Discord ID": int,
                "RSI User": "Test " + str(int),
                "Notes": "",
                "Admitted": False,
                "Submitted": "date here, time here",
                "Updated": ""
                }
            }   

# calling the functions:
log_to_json(new_item)  # will make new log entries
print(parse_from_json(24502273))  # will search for a log given a log_id number (int)
