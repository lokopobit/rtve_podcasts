
## What is this repository?
RTVE is the acronym for "radio television española", that is, the public service for radio and television in Spain. Radio3 is the section dedicated to music, which offers programming 24/7. All the issued radio shows are stored in www.rtve.es under the name podcasts. So, this repository is a scraper of this shows, with its corresponding storing folder structure.

WARNING: www.rtve.es defines a strict robots.txt so that they are NOT crawled. However, I started this project before knowing it so I decided to go on and  create a crawler that:
> does NOT obey robots.txt restrictions.  
> changes the user-agent smartly (with the help of scrapy-fake-useragent library).  
> makes use of IP proxies (only if needed).

NOTE: I do NOT use this crawler. Use it under your own responsability. 

For those willing to download some radio shows but don't want to bother the web server I created scrape_podcasts.py, a script that just downloads one sound file.

## How to Use
> 1. Install the requiered packages: scrapy, pandas and scrapy-fake-useragent. 
> 2. Set up the path where the files will be saved. To do that paste the absolute path of the folder in the variable FILES\_STORE of the settings.py file (rtve\_podcasts/podcasts/podcasts).  
> 3. Paste the podcasts urls inside the self.urls list in the mp3_spider.py script (rtve\_podcasts/podcasts/podcasts/spiders). There are examples provided.
> 4. Open a terminal in the folder rtve\_podcasts/podcasts/podcasts and execute scrapy crawl mp3files.

## Implementation Details
A scrapy spider with 5 seconds delay per download. The filename of the sound files is the date of emission, so a csv file relating the date and the show name is also saved in the folder. Then, the csv are joined into one and the mp3 files compressed with [precomp](https://github.com/schnaader/precomp-cpp).   


## Why did I Decided to Create this Crawler?
I like a lot the music played in these radio shows, so I decided to download them so I could listen to them offline. Before creating this spider I searched if already somebody have done it and uploaded to github. I found one repository ([https://github.com/garciadelcastillo/Documentos-RNE](https://github.com/garciadelcastillo/Documentos-RNE)) but I could not manage to make it work so I opened an issue (the repository was no longer under maintenance and 3 years ago last updated).

## Future work 
I would also like to do some data analysis with all the mp3 files. For example, split them to remove the intro and the talker voice to recover the songs, so that the size can be reduced. To achieve this task I tried music ripping open source available technologies but I was not able to split the audio files as desired. I also tried speaker recognition but any result was achieved. Finally, I will wait to buy a GPU and make the software to split the files by my own. 
