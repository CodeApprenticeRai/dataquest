## 2. Drawing lines ##

import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3, 4, 5]
# Going by our formula, every y value at a position is the same as the x-value in the same position.
# We could write y = x, but let's write them all out to make this more clear.
y = [0, 1, 2, 3, 4, 5]

# As you can see, this is a straight line that passes through the points (0,0), (1,1), (2,2), and so on.
plt.plot(x, y)
plt.show()

# Let's try a slightly more ambitious line.
# What if we did y = x + 1?
# We'll make x an array now, so we can add 1 to every element more easily.
x = np.asarray([0, 1, 2, 3, 4, 5])


# y is the same as x, but every element has 1 added to it.
y = x - 1
plt.plot(x, y)
plt.show()
# This plot passes through (0,1), (1,2), and so on.
# It's the same line as before, but shifted up 1 on the y-axis.

# By adding 1 to the line, we moved what's called the y-intercept -- where the line intersects with the y-axis.
# Moving the intercept can shift the whole line up (or down when we subtract).
y = x + 10
plt.plot(x, y)
plt.show()

## 3. Working with slope ##

import matplotlib.pyplot as plt
import numpy as np

x = np.asarray([0, 1, 2, 3, 4, 5])
# Let's set the slope of the line to 2.
y = 2 * x

# See how this line is "steeper" than before?  The larger the slope is, the steeper the line becomes.
# On the flipside, fractional slopes will create a "shallower" line.
# Negative slopes will create a line where y values decrease as x values increase.
y = 4 * x
plt.plot(x, y)
plt.show()

y = .5 * x
plt.plot(x, y)
plt.show()

y = -2 * x
plt.plot(x, y)
plt.show()

## 4. Starting out with linear regression ##

# The wine quality data is loaded into wine_quality
from numpy import cov

slope_density = cov(wine_quality['density'], wine_quality['quality']) / (wine_quality['density'].var())

## 5. Finishing linear regression ##

from numpy import cov

# This function will take in two columns of data, and return the slope of the linear regression line.
def calc_slope(x, y):
  return cov(x, y)[0, 1] / x.var()

intercept_density = wine_quality['quality'].mean() - (calc_slope(wine_quality['density'],wine_quality['quality'])* wine_quality['density'].mean())

## 6. Making predictions ##

from numpy import cov

def calc_slope(x, y):
  return cov(x, y)[0, 1] / x.var()

# Calculate the intercept given the x column, y column, and the slope
def calc_intercept(x, y, slope):
  return y.mean() - (slope * x.mean())

m = calc_slope(wine_quality["density"], wine_quality["quality"])
b = calc_intercept(wine_quality["density"], wine_quality["quality"], m)

def pred_y(x):
    y = (m * x) + b
    return y

predicted_quality = wine_quality['density'].apply(pred_y)

## 7. Finding error ##

from scipy.stats import linregress

# We've seen the r_value before -- we'll get to what p_value and stderr_slope are soon -- for now, don't worry about them.
slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])

# As you can see, these are the same values we calculated (except for slight rounding differences)
print(slope)
print(intercept)

def pred_y(x):
    y = (slope * x) + intercept
    return y

pred_ys = wine_quality["density"].apply(pred_y)

dif1 = [(pred_ys[i] - wine_quality["quality"][i])**2 for i in range(len(pred_ys))]
rss = sum(dif1)
print(rss)

## 8. Standard error ##

from scipy.stats import linregress
import numpy as np

# We can do our linear regression
# Sadly, the stderr_slope isn't the standard error, but it is the standard error of the slope fitting only
# We'll need to calculate the standard error of the equation ourselves
slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])

predicted_y = np.asarray([slope * x + intercept for x in wine_quality["density"]])
residuals = (wine_quality["quality"] - predicted_y) ** 2
rss = sum(residuals)

std_err = (rss/len(residuals))**(1/2)

def absv(x):
    return (x**2)**(1/2)
def wq_fitness(n):
    ins = [1 for i in range(len(predicted_y)) if (absv(predicted_y[i] - wine_quality["quality"][i])/ std_err) < n]
    return len(ins)/len(predicted_y)

within_one = wq_fitness(1)
within_two = wq_fitness(2)
within_three = wq_fitness(3)
