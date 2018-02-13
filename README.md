# hinativescrap
Scraping [HiNative](https://hinative.com) Users Data

## Usage
I provide my results in file `results_clean.csv`, containing:
- Username (48979 users)
- Native languages
- Languages of interest

There's also `results.csv` - 50000 entries, including users no longer exist, maybe unconfirmed registrations or deleted accounts.
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
6. To clean the data from empty rows, run `cleaning.py`. To reorder the columns run `reordering.py`
7. You can modify `items.py` and `basic.py` to get more informations like Countries they know well, or anything.

## Counting
I count the data, with `counting.py` and the results is listed in `rank_results.txt`. (Well, I was wrong when I said that there were more Korean natives than Arabic, a mistake). From 48979 samples, I got:


### Native languages
| Native Language | Number of Users |
| ----------------| --------------- |
| English (US)                      | 8483 |
| Russian                           | 6596 |
| Arabic                            | 6318 |
| Polish                            | 3764 |
| Portuguese (Brazil)               | 3509 |


### Languages of Interest
| Language of Interest | Number of Users |
| -------------------- | --------------- |
| English (US)                      | 28619 |
| Japanese                          | 11771 |
| Korean                            |  9996 |
| English (UK)                      |  6457 |
| French (France)                   |  4642 |

