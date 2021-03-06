## 1. Introduction ##

strings = ["data science", "big data", "metadata"]
regex = "data"

## 2. Wildcards in Regular Expressions ##

strings = ["bat", "robotics", "megabyte"]
regex = "b.t"

## 3. Searching the Beginnings And Endings Of Strings ##

strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b.tter"

## 5. Reading and Printing the Data Set ##

import csv
posts_with_header = list(csv.reader(open('askreddit_2015.csv','r')))
posts = posts_with_header[1:]

for post in posts:
    print(posts)

## 6. Counting Simple Matches in the Data Set with re() ##

import re

regex = "of Reddit" 
of_reddit_count = 0

for post in posts: 
    if re.search(regex, post[0]) != None:
        of_reddit_count += 1
        print(re.search(regex, post[0]))
    else:
        pass
  

## 7. Using Square Brackets to Match Multiple Characters ##

import re

of_reddit_count = 0
for row in posts:
    if re.search("of [Rr]eddit", row[0]) is not None:
        of_reddit_count += 1

## 8. Escaping Special Characters ##

import re
regex = "\[Serious]"

serious_count = 0
for post in posts:
    if re.search(regex, post[0]) != None:
        serious_count += 1

## 9. Combining Escaped Characters and Multiple Matches ##

import re

serious_count = 0
for row in posts:
    if re.search("\[[Ss]erious]", row[0]) != None:
        serious_count += 1

## 10. Adding More Complexity to Your Regular Expression ##

import re

serious_count = 0
for row in posts:
    if re.search("[\[\(][Ss]erious[\)\]]", row[0]) is not None:
        serious_count += 1

## 11. Combining Multiple Regular Expressions ##

import re

regex = "[\[\(][Ss]erious[\)\]]"

serious_start_count = 0
for post in posts:
    if re.search("^" + regex, post[0]) != None:
        serious_start_count += 1
        
serious_end_count = 0
for post in posts:
    if re.search(regex + "$", post[0]) != None:
        serious_end_count += 1

serious_count_final = 0
for post in posts:
    if re.search("^" + regex + "|" + regex + "$", post[0]) != None:
        serious_count_final += 1


## 12. Using Regular Expressions to Substitute Strings ##

import re
posts_new = []

for post in posts:
    post[0] = re.sub("[\[\(][Ss]erious[\]\)]","[Serious]",post[0])
    posts_new.append(post)
 

## 13. Matching Years with Regular Expressions ##

import re

year_strings = []
for string in strings:
    if re.search("[1-2][0-9][0-9][0-9]", string):
        year_strings.append(string)
        

## 14. Repeating Characters in Regular Expressions ##

import re

year_strings = []

for string in strings:
    if re.search("[0-2][0-9]{3}",string):
        year_strings.append(string)

## 15. Challenge: Extracting all Years ##

import re

years = re.findall("[0-2][0-9]{3}", years_string)