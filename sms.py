headers = {
    "X-Mashape-Key": "KEY"
  }
import requests
message = "Double check. i could spam you you know"
semi_colon = '%3B'
phone = 'xx;xx'
username = 'phonenumber'
password = 'password' #1450
response = requests.get("https://freesms8.p.mashape.com/index.php?msg="+message+"&phone="+phone+"&pwd="+password+"&uid="+username, headers=headers)
print response.status_code
print response.content
