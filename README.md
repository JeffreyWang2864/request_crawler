# urllib_simple_crawler

> last update: 12/06/2017
>
> added threading feature

This is a Python script

A simple crawling program that download restaurant reviews from yelp.com with BeautifulSoup and urllib

you can simply change the starting url in [main.py](https://github.com/JeffreyWang2864/urllib_simple_crawler/blob/master/main.py)
by replacing: 

`root_url = "https://www.example1.com"` to `root_url = "https://www.example2.com"`

---

There are two options for exporting the result ([outputer](https://github.com/JeffreyWang2864/urllib_simple_crawler/blob/master/crawl/outputer.py)): `.html` or `.txt`


in [crawler.py](https://github.com/JeffreyWang2864/urllib_simple_crawler/blob/master/crawl/crawler.py), line 20, You can simply do:

`self.write_method = self.outputer.writeTXT` or `self.write_method = self.outputer.writeTXT`

![alt text](https://github.com/JeffreyWang2864/urllib_simple_crawler/blob/master/images/running.png)
