#coding=utf-8

import sys
import os,shutil
import time

print("样例:python migrate.py /Users/huweijun/dev/opensource/book/javascript  /Users/huweijun/dev/opensource/blog/_posts/javascript")
print("参数列表:"+sys.argv[1])

source_path=sys.argv[1]
target_path=sys.argv[2]
files=os.listdir(source_path)

while files:

    if not target_path.endswith("/"):
        target_path+="/"
    if not os.path.exists(target_path):
        os.makedirs(target_path)
        print(target_path+"已经创建")

    file_name=files.pop()

    if source_path.endswith("/"):
        file_path=source_path+file_name
    else:
        file_path = source_path +"/"+ file_name



    stat = os.stat(file_path)
    if file_name.startswith("."):
        continue

    if os.path.isdir(file_path):
        continue

    # print(file_path, os.path.isdir(file_path))

    file_name_moved= target_path+(time.strftime("%Y-%m-%d",time.gmtime(stat.st_birthtime))+"-"+file_name).replace("_","-")
    print(file_path,file_name_moved)
    shutil.copy(file_path,file_name_moved)