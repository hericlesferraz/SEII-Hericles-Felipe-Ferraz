'''
Aluno: Hericles Felipe Ferraz
Matricula: 11811EMT022
'''

import pytz
import datetime

d = datetime.date(2021, 3, 15)
print(d)

tday = datetime.date.today()

print(tday) 
print(tday.year) 
print(tday.weekday()) 

tday = datetime.date.today()
datetime.timedelta(days=7)
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)

tday = datetime.date.today()
bday = datetime.date(2021, 7, 23)
till_bday = bday - tday
print(till_bday.days) #faltam 130 dias

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

dt = datetime.datetime(2021, 3, 15, 16, 33, 20, tzinfo=pytz.UTC)
print(dt)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)
dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)

print(dt_mtn)
print(dt_mtn.strftime('%B %d, %Y'))

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
dt_str = 'March 15, 2021'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
