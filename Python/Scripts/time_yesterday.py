import datetime 

def getYesterday():
today=datetime.date.today()
oneday=datetime.timedelta(days=1) ##这里是时间精度，时分天
##可以直接进行时间的加减，剪表示过去时间，加表示未来时间
yesterday=today-oneday
return yesterday # 输出 

print(getYesterday())
