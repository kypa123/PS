import re


def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    new_id = re.sub(r'\.{2,}', '../programmers', new_id)
    new_id = re.sub(r'^\.|\.$', '', new_id)
    if new_id == "":
        new_id = "a"
    elif len(new_id) >= 16:
        new_id = new_id[:14]
        return new_id
    elif len(new_id) < 3:
        word = new_id[-1]
        while len(new_id) < 3:
            new_id += word
    return new_id