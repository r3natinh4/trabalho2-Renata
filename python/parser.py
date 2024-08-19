import re

def parse_txt(filepath):
    data = {}
    last_id  = '-1'
    
    with open(filepath, 'r') as file:
        content = [item.strip() for item in file.readlines() if item.strip() != '']
    
    for line in content:
        match = re.match(r'([a-zA-Z0-9_\-]+)(?:\s+)?(?::)(?:\s+)?(.+)', line)
        
        if match is None:
            continue
        
        key_name  = match.group(1)
        key_value = match.group(2)
        
        if key_name == 'id':
            last_id = key_value
            data[key_value] = {}
        else:
            data[last_id][key_name] = key_value
    
    return data
