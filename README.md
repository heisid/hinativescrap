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
pip install scrapy
```
4. Play with range of users id (I don't know the correct term for this, I refer to unique integer numbers in users profile URL) in `hinative/spiders/basic.py`. Look at variable `user_range`.
Warning: Don't be greedy, once I crawled 100,000 pages and got my IP blacklisted.
5. Run it!
```shell
scrapy crawl basic -o filename.csv
```
6. To clean the data from empty rows, run `cleaning.py`. To reorder the columns run `reordering.py`
7. You can modify `items.py` and `basic.py` to get more informations like Countries they know well, or anything.
8. To make your life easier, install pandas to analyze further.
```shell
pip install pandas
```

## Counting
I count the data, with `counting.py` and the results is listed in `rank_results.txt`. (Well, I was wrong when I said that there were more Korean natives than Arabic, a mistake). From 48979 samples, I got:


### Native languages
| Native Language | Number of Users | Percentage |
| ----------------| --------------- | ---------- |
| English (US)                      | 8483 | 17.320% |
| Russian                           | 6596 | 13.467% |
| Arabic                            | 6318 | 12.899% |
| Polish                            | 3764 |  7.685% |
| Portuguese (Brazil)               | 3509 |  7.164% |


### Languages of Interest
| Language of Interest | Number of Users | Percentage |
| -------------------- | --------------- | ---------- |
| English (US)                      | 28619 | 58.431% |
| Japanese                          | 11771 | 24.033% |
| Korean                            |  9996 | 20.409% |
| English (UK)                      |  6457 | 13.183% |
| French (France)                   |  4642 |  9.478% |

