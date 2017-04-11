## 4. Querying a SQLite Database ##

SELECT Rank,Major
from recent_grads;

## 5. Specifying Column Order for Our Results ##

Select Major,Rank
From recent_grads;


## 6. Practice: Selecting Columns With SELECT ##

SELECT Rank,Major_code,Major,Major_category,Total
from recent_grads;


## 7. Filtering With the WHERE Statement ##

SELECT Major,ShareWomen
From recent_grads
Where ShareWomen > 0.5;

## 8. Practice: Filtering With WHERE Statements ##

SELECT Major,Employed
from recent_grads
where Employed > 10000;

## 9. Limiting the Number of Results ##

SELECT Major FROM recent_grads WHERE Employed > 10000 LIMIT 10;