## 3. The Math Module ##

import math

a = math.sqrt(16.0)
b = math.ceil(111.3)
c = math.floor(89.9)

## 4. Variables Within Modules ##

import math

print(math.pi)
mpi = math.pi
a = math.sqrt(mpi)
b = math.ceil(mpi)
c = math.floor(mpi)


## 5. The CSV Module ##

import csv
nfl = list(csv.reader(open("nfl.csv")))

## 6. Counting How Many Times a Team Won ##

import csv

rdata = list(csv.reader(open("nfl.csv")))
#print(rdata)

patriots_wins = 0

for row in rdata:
    if 'Patriots' in row[2]:
        patriots_wins += 1
        
print("During the years 2009 - 2013, the patriots have won %r times." % patriots_wins)


## 7. Making a Function that Counts Wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.
def nfl_wins(team_name):
    team_wins = 0
    for row in nfl:
        if team_name in row[2]:
            team_wins += 1
        
    print("During the years 2009 - 2013, the {} have won {} times.".format(team_name, team_wins))
    return(team_wins)    
        
cowboys_wins = nfl_wins("Dallas Cowboys")
falcons_wins = nfl_wins("Atlanta Falcons")

print(cowboys_wins)

## 10. Working with Boolean Operators ##

a = 5
b = 10
# a == 5
result1 = True

# a < 5 or b > a
result2 = True

# a < 5 and b > a
result3 = False

# a == 5 or b == 5
result4 = True

# a > b or a == 10
result5 = False

## 11. Counting Wins in a Given Year ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

def nfl_wins_in_a_year(team, year):
    count = 0
    year = int(year)
    for row in nfl:
        if (row[0] == year) and (row[2] == team):
            count = count + 1
    return(count, year)

browns_2010_wins = nfl_wins_in_a_year("Cleveland Browns", 2010)
eagles_2011_wins = nfl_wins_in_a_year("Philadelphia Eagles", 2011)
