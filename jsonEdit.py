import json

def read_json(path):
    with open(path, "r") as read_content:
        return json.load(read_content)



def write_json(path, data): 
    with open(path, "r") as read_content:
        old_data = json.load(read_content)

    merge_dic = dict(old_data, **data)


    with open(path, 'w') as file:
        json.dump(merge_dic, file)

