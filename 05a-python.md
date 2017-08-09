# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both ordered collections of objects, but lists are mutable and tuples are not. In general, the elements of a tuple represent heterogenous types of objects with a certain structure that will be unpacked, e.g. a date is often represented as a tuple in the form `(2017, 08, 09)`. The elements of a list represent the same objects in a certain order, e.g. a list of numbers `[0, 1, 2, 3, 4, 5]`. Tuples will work as dictionary keys while lists will not, because dictionary keys are required to be hashable. All immutable objects in Python are hashable.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both mutable collections of objects, but used differently. Unlike lists, sets are unordered, and can only contain elements that are hashable. Sets do not contain duplicate elements. Sets also cannot be sliced. Sets in Python are implemented as hash table (which is why their elements must be hashable), which makes membership testing much faster than in lists, which are implemented as dynamic arrays.  
>> Examples:
>> * List: `dice_rolls = [4, 3, 1, 5, 4, 6]`, a list of rolls of a die in the sequence they were made. Additional rolls can be added to the end of the list with `dice_rolls.append(n)`.  
>> * Set: `map_colors = set(['red', 'blue', 'green', 'orange'])`, a set of colors used in drawing a map. The order of colors in the set doesn't matter. It also doesn't make sense for there to be duplicate entries.  

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





