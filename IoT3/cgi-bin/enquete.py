#!/usr/bin/python3
# for form1.html sample program

import cgi

# ヘッダーを送出する関数
def send_header():
    print("Content-Type: text/html; charset=utf-8")
    print("")

# インスタンス作成
form = cgi.FieldStorage()

send_header()
# print(form)

infos = ["email", "course", "comment", "id", "submit"]
jobs = form.getvalue("job")
# print(type(form.getvalue("job")))
for info in infos:
  print(info+": "+form.getvalue(info))
  print("<br>")
  
print("Jobs: ")
for job in jobs:
  print(job)