[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> We are asked to investigate whether the results given by the function `random.random` are truly random. If so, the generated numbers should have a uniform distribution. By generating 1000 "random" numbers, we can examine the PMF and the CDF to see if this is the case. The PMF should look like a horizontal line on the domain (0 to 1) and the CDF should be a straight line representing y=x, from (0, 0) to (1, 1), since we are looking at percentile ranks.
 
We first generate the random numbers with: `num_list = [np.random.random() for x in range(1000)]`

Then, we can plot the PMF (using the supplied class and plot functions) with: 
```
pmf = thinkstats2.Pmf(num_list)
thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Random Numbers', ylabel='PMF')
```
 
[Insert PMF Plot here]

The problem with using the PMF to assess the distribution is that with so many values, it's hard to visually determine where any peaks and valleys are. We can mitigate this by looking at the CDF instead, which maps each value to its percentile rank in the distribution.

```
cdf = thinkstats2.Cdf(num_list)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Random Numbers', ylabel='CDF')
```
 
[Insert CDF Plot Here]

We see that the CDF is indeed (approximately) a straight line, so the distribution of values is uniform. This doesn't necessarily mean that the values are truly random, but the distribution does not seem to be biased in any way.
