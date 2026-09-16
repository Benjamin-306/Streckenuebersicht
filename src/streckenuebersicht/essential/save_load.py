import json

def load(path):
    try:
        with open(path, "r", encoding = "utf-8") as f:
            data = json.load(f)
    except:
        data = {}

    return data

def save(path, data):
    with open(path, "w", encoding = "utf-8")as f:
        json.dump(data, f, indent = 4)