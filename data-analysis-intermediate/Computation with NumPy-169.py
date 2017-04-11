## 2. Array Comparisons ##

years_1984 = (world_alcohol[:,0]  == '1984')

countries_canada = (world_alcohol[:,2] == "Canada")
                               

## 3. Selecting Elements ##

country_is_algeria = (world_alcohol[:,2] == "Algeria")
country_algeria = world_alcohol[country_is_algeria,:]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = (world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Algeria')

rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]



## 5. Replacing Values ##

world_alcohol[:,0][world_alcohol[:,0] == '1986'] = '2014'


c2 = world_alcohol[:,3] == 'Wine'
world_alcohol[c2,3] = 'Grog'

## 6. Replacing Empty Strings ##

is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty,4] = '0'

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4]
alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

c1 = (world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Canada')
canada_1986 = world_alcohol[c1,:]

canada_alcohol = canada_1986[:,4]
c2 = canada_alcohol == ''
canada_alcohol[c2] = '0'
total_canadian_drinking = canada_alcohol.astype(float).sum()


## 10. Calculating Consumption for Each Country ##

totals = {}

c1 = world_alcohol[:,0] == '1989'
m1 = world_alcohol[c1]

for c in countries:
    tcon1 = m1[:,2] == c
    country_match = m1[tcon1]
    tcon2 = country_match[:,4] == ''
    country_match[tcon2] = '0'
    nums = country_match[:,4].astype(float)
    country_total = nums.sum()
    totals[c] = country_total
        
print(totals)

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None

for key, value in totals.items():
    if value > highest_value:
        highest_value = value
        highest_key = key

