import os
number=0
path=r'C:\Users\姜\Desktop\python\log_files'
content=os.listdir(path)
for file in content:
    with open(path+'//'+file,encoding='utf8') as f:
       for line in f:
         if '课程：python, 学号：201811123030, 时间：2019-04-29T16:15:33.400728' in line:
           number=number+1

print("该同学的打卡次数为：",number)