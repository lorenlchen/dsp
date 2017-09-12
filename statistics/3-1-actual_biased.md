[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> We are asked to examine the effect of the class-size paradox when looking at the number of children per family. The class-size paradox in this example is that there will be a bias between your result when you ask a mom how many children she has compared to asking the children in the same population how many siblings each has. This is because larger families will be over-represented in the data. We can examine this difference using the supplied function `BiasPMF`, defined as:
```
def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
```
First, we can plot the actual distribution of number of children by reading in the relevant data and then plotting the PMF.
```
resp = nsfg.ReadFemResp()
actual = thinkstats2.Pmf(resp.numkdhh, label='actual')
thinkplot.Pmf(actual)
thinkplot.Config(xlabel='Number of children', ylabel='PMF')
```
The resulting plot:
 
![3.1 Actual Plot](https://github.com/lorenlchen/dsp/blob/master/img/3_1_actual_plot.png)
 
Then, we can bias the data using the above function and plot the new PMF on the same graph.
```
biased = BiasPmf(actual, label='biased')
thinkplot.PrePlot(2)
thinkplot.Pmfs([actual, biased])
thinkplot.Config(xlabel='Number of children', ylabel='PMF')
```
The resulting plot:
 
![3.1 Actual vs. Biased Plot](https://github.com/lorenlchen/dsp/blob/master/img/3_1_biased_plot.png)
 
As we can see, the biased PMF is shifted right from the actual distribution. A notable thing is that in the biased distribution, it seems like there are no families with 0 children, since there would be no one to ask how many siblings they have. While the actual plot is monotone decreasing, the biased plot has a peak in the middle.

