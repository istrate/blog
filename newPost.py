import json
filename = 'posts.json'
entry = {"model": "blog.post","pk": 3,"fields": {"author": 1,"title": "Set from build-hook","text": " Command worked succesfully","created_date": "2021-10-10T03:26:20.023Z","published_date": "2021-10-10T03:26:20.026Z"}}
# 1. Read file contents
with open(filename, "r") as file:
    data = json.load(file)
# 2. Update json object
data.append(entry)
# 3. Write json file
with open(filename, "w") as file:
    json.dump(data, file)
