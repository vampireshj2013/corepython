import datetime
import time

print datetime.date.today()
print datetime.date.fromtimestamp(time.time())
date = datetime.date(2017, 5, 9)

print date.weekday()
print date.isoweekday()
print date.isocalendar()
print date.isoformat()
print time.time()

date7 = date.replace(day=7)
timedelt = (date - date7)
print timedelt.days
print timedelt.seconds
print timedelt.microseconds

tm = datetime.time(23,46,10)
print tm
print "hour:%d,minutu:%d,seconds:%d,microseconds:%s"\
    % (tm.hour,tm.minute,tm.second,tm.microsecond)
tm1 = tm.replace(hour=20)
print "tm1", tm1
print "tm1format:",tm1.isoformat()

print "datetime.datetime.now()",datetime.datetime.now()
print "datetime.datetime.now()",datetime.datetime.utcnow()


dt = datetime.datetime.now()
print dt.strftime("%Y-%m-%d %H:%M:%S")
print dt.strptime("2017-05-10 23:07:45","%Y-%m-%d %H:%M:%S")

date1Str = "05/10/17"
date2Str = "05/08/17"

fmt = "%m/%d/%y"

t1 = datetime.datetime.strptime(date1Str,fmt)
t2 = datetime.datetime.strptime(date2Str,fmt)
print t1,t2
print (t1 -t2).days

birthday = datetime.datetime(1992,8,9)
print birthday
now = datetime.datetime.now()
next_birthday = now.replace(month=birthday.month,day=birthday.day)
if (next_birthday-now).seconds > 0:
    print (next_birthday-now).days
else:
    next_birthday.replace(year=next_birthday.year+1)
    print (next_birthday - now).days
