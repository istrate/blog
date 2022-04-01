import sys

print('"**********************mailer script started here"**********************')

with open('posts.json', 'w') as f:
    print('[{"model": "blog.post","pk": 1,"fields": {"author": 1,"title": "Does this work?","text": "It looks like it does","created_date": "2022-03-14T03:26:20.023Z","published_date": "2022-03-14T03:26:20.026Z"}}]', file=f)
print("Post done successfully")
print("**************************Hook worked successfuly***********************")
