# imports, both are built-in modules
import json
import random
from datetime import datetime


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
def searchby_message(message_id):
    f = open("logs.json", mode='r', encoding='utf-8')
    data_list = json.load(f)
    index = 0
    while index < len(data_list):
        if data_list[index]["log_id"] == message_id:
            return data_list[index]
        index += 1


# lets us change anything under the "data" section in the json
def change_log(message_id, data_key, new_value):
    f = open("logs.json", mode='r', encoding='utf-8')  # open json
    data_list = json.load(f)  # get data stream
    index = 0
    while index < len(data_list):
        if data_list[index]["log_id"] == message_id:
            data_list[index]["data"][data_key] = new_value
            data_list[index]["data"]["Updated"] = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
        index += 1
    f = open("logs.json", mode='w', encoding='utf-8')
    json.dump(data_list, f, indent=2)
    

# search for user id, note: will return first object found
def searchby_user(user_id):
    f = open("logs.json", mode='r', encoding='utf-8')
    data_list = json.load(f)
    index = 0
    while index < len(data_list):
        if data_list[index]["data"]["Discord ID"] == user_id:
            return data_list[index]
        index += 1
    

# manually add a log entry given the message id and the user id, everything else is optional
def manual_log_to_json(message_id, user_id, discord_username="", rsi_username="", notes="", admitted=None):
    entry = {"log_id": message_id,
            "data": {
                "Discord User": discord_username, 
                "Discord ID": user_id, 
                "RSI User": rsi_username, 
                "Notes": notes, 
                "Admitted": admitted, 
                "Submitted": datetime.now().strftime('%m/%d/%Y, %H:%M:%S'), 
                "Updated": ""
                }
        }
    
    with open("logs.json", mode='r', encoding='utf-8') as f:
        feeds = json.load(f)
            
    with open("logs.json", mode='w', encoding='utf-8') as feedsjson:
        feeds.append(entry)        
        json.dump(feeds, feedsjson, indent=2)



# EXAMPLES:
'''
# this just makes random entries for me to demonstrate with:
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

#log_to_json(new_item)  # will make new log entries
#print(searchby_message(901815455185002558))  # will search for a log given a log_id number (int)
#change_log(901815455185002558, "Admitted", True)
print(searchby_user(2043397889945763842))
manual_log_to_json(123456789101112131415, 2043397889945763842, notes="Test success.", discord_username="Stinky Rat Boy")  
print(searchby_user(2043397889945763842))
'''
