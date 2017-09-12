[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> We want to know what percentage of the male population meets the height requirement to be in the Blue Man Group, assuming that height is distributed normally. We create a normally ditrbuted variable in `scipy.stats` with:
```
mu = 178
sigma = 7.7
height = scipy.stats.norm(loc=mu, scale=sigma)
```
The Blue Man Group requires that performers be between 5'10 and 6'1. First, we need to convert these heights to centimeters. Then, we can find the percentage of men that meet this requirement by subtracting the cdf of the lower bound from that of the upper bound.
```
inches_to_cm = 2.54
low_height = 70 * inches_to_cm
high_height = 73 * inches_to_cm
height.cdf(high_height)-height.cdf(low_height)
```
From this, we find that about 34.3% of men would meet this height requirement.
