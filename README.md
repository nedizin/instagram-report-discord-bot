# InstagramReport
An selenium application to auto report an account based on a discord bot made in python.

Example for using multiple accounts:
```python

browser1 = webdriver.Firefox()
browser2 = webdriver.Firefox()
browser3 = webdriver.Firefox()
browser4 = webdriver.Firefox()

contas = [["email@gmail.com", "pass", browser1], ["email2@gmail.com", "pass", browser2], ["email3@gmail.com", "pass", browser3], ["email4@gmail.com", "pass", browser4]]

```

Used librarys:
```
selenium
os
urllib.request
string
random
time
requests
discord
```
