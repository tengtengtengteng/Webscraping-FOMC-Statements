from bs4 import BeautifulSoup
import requests
import pandas as pd

# define the url of fomc calendars
base_url = "http://www.federalreserve.gov"
date_url = "/monetarypolicy/fomccalendars.htm"
# get response from the website
date_resp = requests.get(base_url + date_url)
date_soup = BeautifulSoup(date_resp.content, 'lxml')

# find the meeting dates 
meetings = date_soup.find_all('div', class_ = 'col-xs-12 col-md-4 col-lg-2')

#save the urls into a list
statement_url_list = []
for meeting in meetings:
    try:
        statement = meeting.find('a', text = 'HTML')
        if statement:
            #print(statement)
            statement_url = statement['href']
            statement_url_list.append(statement_url)
            #print('ok')
    except AttributeError:
        continue

# get those not found in the FOMC calendar page -> moved to historical
historical_url = "/monetarypolicy/fomchistorical{}.htm"
for year in range(2015,2011,-1):
    year_resp = requests.get(base_url + historical_url.format(year))
    year_soup = BeautifulSoup(year_resp.content, 'lxml')
    # find the links
    links = year_soup.find_all('div', class_ = 'col-xs-12 col-md-6')
    for link in links:
        # find the statement's url
        try:
            statement = link.find('a', text = 'Statement')
            if statement:
                #print(statement)
                statement_url = statement['href']
                statement_url_list.append(statement_url)
                #print('ok')
        except AttributeError:
            continue


# go to each url and save the date and article
date_list = []
statement_list = []
for statement_url in statement_url_list:
    statement_resp = requests.get(base_url + statement_url)
    statement_soup = BeautifulSoup(statement_resp.content, 'lxml')
    # get the article and date
    article = statement_soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').text
    date = statement_url[-13:-5]
    statement_list.append(article.strip())
    date_list.append(date)
# save as df
df_statements = pd.DataFrame(list(zip(date_list, statement_list)), 
                             columns =['Date', 'Statement'])
# convert date to date format
df_statements['Date'] = pd.to_datetime(df_statements['Date'], format='%Y%m%d')
# sort by date
df_statements.sort_values(by='Date', ascending=False, inplace=True)
# output to csv
df_statements.to_csv('FOMC_statements.csv', index=False, encoding='utf-8-sig')

