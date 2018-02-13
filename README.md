# hinativescrap
Scraping [HiNative](https://hinative.com) Users Data

## Usage
I provide my results in file `results_clean.csv`, containing:
- Username (48980 users)
- Native languages
- Languages of interest
There's also `results.csv` - 50000 entries, including non-existent users, maybe unconfirmed registrations or deleted accounts.
It took about 2 hours to collect the data.
 
Just in case you want to try scraping by yourself
1. Install Python 3, venv, and pip
2. Create virtual environment
```shell
python -m venv env
source env/bin/activate
```
3. Install Scrapy
```shell
pip install Scrapy
```
4. Play with range of users id (I don't know the correct term for this, I refer to unique integer numbers in users profile URL) in `hinative/spiders/basic.py`. Look at variable `user_range`.
Warning: Don't be greedy, once I crawled 100,000 pages and got my IP blacklisted.
5. Run it!
```shell
scrapy crawl basic -o filename.csv
```
6. To clean the data from empty row, run `cleaning.py`
7. You can modify `items.py` and `basic.py` to get more informations like Countries they know well, or anything.
