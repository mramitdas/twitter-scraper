# Twitter Scraper

![GitHub](https://img.shields.io/github/license/mramitdas/twitter-scraper) ![GitHub contributors](https://img.shields.io/github/contributors/mramitdas/twitter-scraper) ![code size](https://img.shields.io/github/languages/code-size/mramitdas/twitter-scraper) ![maintain status](https://img.shields.io/maintenance/yes/2022)

A scraping tool to scrape tweets from user timeline.

You can use this to get the text of any user's Tweets trivially.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* Internet Connection
* Python 3.6+

## Installing twitter-scraper

If you want to use latest version, install from source. To install twitter-scraper from source, follow these steps:

Linux and macOS:
```bash
git clone https://github.com/mramitdas/twitter-scraper.git
cd twitter-scraper
pip3 install -r requirements.txt
python3 app.py 
```

## Using twitter_scraper

Just import **twitter_scraper** and call functions!

### → class **TwitterScrapper(config_file)** -> output.csv

```python
Python 3.9.5 (default, May  3 2021, 19:12:05) 
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from twitter_scraper import TwitterScrapper
>>> 
>>> TwitterScrapper('config.ini')
... 
…
```

It returns a csv file
```csv
Serial,Time,Id,Name,Tweet
1,2022-08-30 09:02:23+00:00,1564539016032034816,AajTak,Tweet1
2,2022-08-30 08:58:23+00:00,1564538008606425088,AajTak,Tweet2
3,2022-08-30 08:49:08+00:00,1564535678729617408,AajTak,Tweet3
4,2022-08-30 08:48:48+00:00,1564535596668059648,AajTak,Tweet4
5,2022-08-30 08:48:06+00:00,1564535420255629312,AajTak,Tweet5
```

## Project Structure
```
|   main.py
|   config.ini
|   README.md
|   requirements.txt
```

## Give it a star 
Did you find this information useful, then give it a star 

## Credits
All the credits to [mramitdas](https://github.com/mramitdas)
