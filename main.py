import json

def log_to_json(dict):
    with open("user_logs_dump.json", mode='r', encoding='utf-8') as f:
            feeds = json.load(f)
            
    with open("user_logs_dump.json", mode='w', encoding='utf-8') as feedsjson:
        entry = dict
        feeds.append(entry)        
        json.dump(feeds, feedsjson, indent=2)
        
def parse_from_json(message_id):
    f = open("user_logs_dump.json", mode='r', encoding='utf-8')
    data_list = json.load(f)
    index = 0
    while index < len(data_list):
        if data_list[index]["log_id"] == message_id:
            return data_list[index]
        index += 1
    #print(data_list[0][f'{message_id}'])
    
        
#log_to_json({"user_id": {"id": 21574}})
print(parse_from_json(894307364990251079))
