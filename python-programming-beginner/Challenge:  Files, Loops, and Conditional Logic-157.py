## 3. Read the File Into a String ##

file = open('dq_unisex_names.csv', 'r')

names = file.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()

names_list = names.split("\n")

first_five = names_list[0:5]

print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')

nested_list = [] 

for q in names_list:
    f = q.split(",")
    nested_list.append(f)
    
print(nested_list[0:5])

## 6. Convert Numerical Values ##

print(nested_list[0:5])

numerical_list = []

for q in nested_list:
    f = str(q[0])
    g = float(q[1])
    nl = []
    nl.append(f)
    nl.append(g)
    numerical_list.append(nl)
    
print(numerical_list[0:5])
    

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]

thousand_or_greater = []

for q in numerical_list:
    if q[1] > 1000:
        thousand_or_greater.append(q[0])
        
print(thousand_or_greater[0:10])