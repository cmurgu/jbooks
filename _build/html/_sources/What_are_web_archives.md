# What are web archives?

Have you ever used the Way Back machine to reload a webpage that is no longer available? If you haven't, try searching for your favourite website below, and navigate back in time to a previous version of the web page:

<iframe src="https://archive.org/web/" style="border:0px #ffffff none; margin: auto;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="400px" width="600px" allowfullscreen></iframe>

The WayBack machine captures websites using crawlers that package a webpage's content into a container called a .WARC file (Web Archive file). A WARC file is a lot like a zip file: it contains a lot of information about the web page, including content (text, images), markup and code (HTML, CSS, JS, etc), and additional metadata (when was the crawl completed, by whom). The WayBack Machine essentially opens up the WARC file and attempts to reload the webpage in the browser based on the data included in the WARC file. 

<iframe src="https://calmurgu.com/whats-the-hype/index.html" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="400px" width="600px" allowfullscreen></iframe>

Reloading a WARC file is not a perfect reproduction: certain elements, such as video, are often excluded.

## Web archive process

There are a few ways to create web archives. For example, you can archive websites by asking the WayBack machine to save a website for you. Alternatively, you could use a browser extension like <a href="http://matkelly.com/warcreate/">WarcCreate</a> or software like <a href="https://webrecorder.io/">WebRecorder</a> to create your own web archives through manual crawling. However, the most common approach is to use piece of software called a "crawler." A crawler received crawling instructions from an individual, and proceeds to crawl the web at specific rates. The main component necessary for a crawler to work is a "seed url": a URL for the crawler to start it's crawling journey. From there, the crawler may have instructions to jump from link to link, capturing web pages indiscriminately. Web archivists usually have a specific set of instructions that are within a crawling scope (for example, “these URLS are okay, stay away from these ones”). 

## Test your understanding