import json
import codecs
from typing import List
import numpy as np

def parse_messages(messages_path: str) -> List[List[str]]:
    with open(messages_path, encoding='utf-8') as f:
        raw_conversation = json.loads(f.read())
    
    lines=[]
    for message in raw_conversation['messages']:
        author = message.get('sender_name', '').encode('latin1').decode('utf8')
        text = message.get('content', '').replace('\t', ' ').replace('\n', ' ').replace('\r', ' ').encode('latin1').decode('utf8') 
        time = message['timestamp_ms']
        msg_type = message['type']
        lines.append([author, time, text, msg_type])

    return lines
    
def count_authors(parsed_conversation: np.ndarray, exclude: List[str]) -> int:
    unique_authors = np.unique(parsed_conversation[:, 0])
    filtered_authors = [x for x in list(unique_authors) if x not in exclude]
    return len(filtered_authors)
