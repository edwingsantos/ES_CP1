#ES 1 boolangs


import time 
import datetime as date


current_time = time.time()
readable_time = time.ctime()
new_current_time = date.datetime.now()
hour= new_current_time.strftime("%H")
print(new_current_time)
print(hour)
print(f"current time since january first 1970: {current_time}")

print(f" {readable_time}")
print(f"The hour is saved as an integer: {isinstance(hour, int)}")
print(f"The hour is saved as an float: {isinstance(hour, float)}")
print(f"The hour is saved as an string: {isinstance(hour, str)}")
print(hour.isalpha())
#minutes = %M
#weekend = %A, %a
#day = %d
#month =%B, %b
print(f"Hour has a value: {bool('edwing')}")
 

print(new_current_time)