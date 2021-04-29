# Webscraping-FOMC-Statements
Learning webscraping by attempting to scrape FOMC Statements from 2012 onwards.

This exercise was part of an assignment for an internship application.


## Without Selenium

Using mainly ```BeautifulSoup``` and ```Requests```, I created a list that contained all the url to FOMC Statements from 2016 onwards from [FOMC calendars](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm). For meetings before 2016, they were archived and I noticed that the url had the pattern "/monetarypolicy/fomchistorical{year}.htm". Hence, I looped through each year from 2012 to 2015 and continued appending to the list of urls. Finally, I looped through the list of urls to scrape the articles and output as a csv file.

While this method managed to achieve the objective of scraping FOMC statements from 2012 onwards, it feels like hard-coding to me. Every year, the website is likely to update the list of years to show on the FOMC calendars webpage and archive the latest year. Hence, I decided to attempt this problem again using ```Selenium```.

## With Selenium

All the materials to be scraped can actually be found on [FOMC Materials](https://www.federalreserve.gov/monetarypolicy/materials/) but requires a method to interact with the javascript application on the webpage. With ```Selenium```, this is possible. Using my script, I first updated my desired start date (*01/01/2012*) and selected only the *Policy Statements* checkbox before applying the filter. Then I found out the last page number in the javascript application panel and start looping through each page and getting the url to each FOMC statement. Finally, I looped through the list of urls to scrape the articles and output as a csv file.

