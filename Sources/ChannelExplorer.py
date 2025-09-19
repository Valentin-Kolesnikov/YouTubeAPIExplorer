from time import sleep
import re

def get_info():
    sleep(0.6)
    NameId = input("\nEnter the link with UC... or @... to the channel: ")
    NameId = NameId.strip()
    while True:
        for_id = re.search(r"(UC[\w-]{22})", NameId)
        if for_id:
            return for_id.group(1), None
        
        for_handle = re.search(r"@[\w.-]+", NameId)
        if for_handle:
            return None, for_handle.group(0)

        NameId = input("\nEnter again: ")