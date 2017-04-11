## 2. Parsing the File ##

f = open("la_weather.csv", "r")
data = f.read()

data2 = data.split("\n")

weather_data = []

for q in data2:
    m = q.split(",")
    weather_data.append(m)

print(weather_data)


## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []

for row in weather_data:
    weather.append(row[1])

print(weather)

## 4. Counting the Items in a List ##

count = 0

for x in weather:
    count += 1

print( count == len(weather) )

## 5. Removing the Header ##

new_weather = weather[1:366]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

cat_found = "cat" in animals

space_monster_found = "space_monster" in animals 


## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]


weather_type_found = []

for x in weather_types:
    r = x in new_weather
    weather_type_found.append(r)

print(weather_type_found)

