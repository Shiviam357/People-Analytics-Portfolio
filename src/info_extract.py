import re

def find_email(text):
    # This pattern looks for: [chars] @ [chars] . [chars]
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(pattern, text)
    return match.group() if match else "Not Found"

import re

def find_phone(text):
    # 1. Flexible regex search
    pattern = r'\b\+?[\d\s\-\(\).]{10,20}\b'
    match = re.search(pattern, text)
    
    if match:
        candidate = match.group().strip()
        # 2. Ultimate Cleanse for validation
        clean = candidate.replace("-","").replace(".","").replace("(","").replace(")","").replace(" ","")
        
        # 3. Validation check
        if 10 <= len(clean) <= 15:
            return candidate 
    return "Not Found"
