# rtve_podcasts
Scraper of the podcasts of radio3 (music) of www.rtve.es  

## What is this repository?
RTVE is the acronym for "radio television española", that is, the public service for radio and television in Spain. Radio3 is the section dedicated to music, which offers programming 24/7. All the issued radio shows are stored in www.rtve.es under the name podcasts. So, this repository is a scraper of this shows, with its corresponding storing folder structure.

WARNING: www.rtve.es defines a strict robots.txt so that they are NOT crawled. However, I started this project before knowing it so I decided to go on and  create a crawler that:
> does NOT obey robots.txt restrictions.  
> changes the user-agent smartly (with the help of scrapy-fake-useragent library).  
> makes use of IP proxies (only if needed).

NOTE: I do NOT use this crawler. Use it under your own responsability. 

For those willing to download some radio shows but don't want to bother the web server I created scrape_podcasts.py, a script that just downloads one sound file.

## How to Use

## Implementation Details

## Why did I Decided to Create this Crawler?
