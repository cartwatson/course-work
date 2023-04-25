# 0.  From Problem Analysis to Data Definitions

**Program needs to be made recursive.**

**Needs to handle specific cases: invalid URL is supplied by user, it finds an invalid link, it finds a content tag, it has gone further down the rabbit hole than it needs to.**


# 1.  System Analysis

**No formulas**

**Program gets input from command line as a URL and an optional number to specify recursion depth**

**Output is given as text in the console. No files or graphics created.**

# 2.  Functional Examples

**Good input consists of an absolute URL, bad input is a relative or incomplete URL**

|Good Input                             | Bad Input
|---------------------------------------|--------------------
| https://usu.edu                       | usu.edu
| https://unnovative.net/level0.html 20 | .net

# 3.  Function Template

**Done on paper**


# 4.  Implementation

**Changed program to be recursive.**


# 5.  Testing

**Run python /PATH/TO/crawler.py**
**Program should exit with error specifying what went wrong.**

**Run python /PATH/TO/crawler.py <invalid URL>**
**Program should exit with error specifying what went wrong.**

**Run python /PATH/TO/crawler.py <valid URL>**
**Program should display all links on the site to 3 levels deep**

**Run python /PATH/TO/crawler.py <valid URL> 10**
**Program should display all links on the site to 10 levels deep**
