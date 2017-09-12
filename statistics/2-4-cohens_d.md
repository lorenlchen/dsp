[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> We are asked to find Cohen's d to look at the weight difference between first babies and others. We can use Downey's supplied function, `CohenEffectSize` to find this value. That function is defined as such:
 
```
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d
 ```

We pass the measures to compare weight to this function with: `CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)` and get a result of -0.089. This means that the average weight of first babies is 0.089 (pooled) standard deviations lower than that of other babies. This effect size is larger than the d for the pregnancy length difference. Using `CohenEffectSize(firsts.prglngth, others.prglngth)`, we have a result of 0.029, meaning that first babies have a slightly longer pregnancy than others. The effect size for birth weight is about 3 times larger (in magnitude) than the effect size for pregnancy length, as measured by Cohen's d.
