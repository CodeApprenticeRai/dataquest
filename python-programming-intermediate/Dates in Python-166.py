## 1. The Time Module ##

import time

current_time = time.time()

print(current_time)

## 2. Converting Timestamps ##

import time

current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour

print(current_hour)

## 3. UTC ##

import datetime

current_datetime = datetime.datetime.now()

current_year = current_datetime.year

current_month = current_datetime.month
print(current_datetime)


## 4. Timedelta ##

import datetime

today = datetime.datetime.now()

diff = datetime.timedelta(days = 1)

tomorrow = today + diff
yesterday = today - diff

## 5. Formatting Dates ##

import datetime

mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print(mystery_date_formatted_string)

## 6. Parsing Dates ##

import datetime

mystery_date = mystery_date.strptime("12:00AM on Thursday January 02, 2003","%I:%M%p on %A %B %d, %Y")

## 8. Reformatting Our Data ##

import datetime

type(post[2])
print(post[2])
for post in posts:
    post[2] = datetime.datetime.fromtimestamp(float(post[2]))
    
    

## 9. Counting Posts from March ##

march_count = 0
for post in posts:
    if post[2].month == 3:
        march_count += 1
   

## 10. Counting Posts from Any Month ##


def month_count(month: int):
    month_count = 0
    for row in posts:
        if row[2].month == month:
            month_count += 1
    return month_count

feb_count = month_count(2)
aug_count = month_count(8)