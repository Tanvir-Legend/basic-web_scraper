import requests
from bs4 import BeautifulSoup

id = input("Username: ")
password = input("Password: ")

if id == "pixepic" and password == "wxkipq":
    link = input("Input Your URL: ")
    page = requests.get(link)  
    
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup)
    else:
        print("Failed to retrieve the URL. Check the URL and try again.")
else:
    print("Invalid Username or Password")
