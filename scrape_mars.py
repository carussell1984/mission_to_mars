
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time


def init_browser():
    executable_path = {"executable_path": "../../chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

mars_information = {}
def scrape_news():
    

    #get back most recent articles from mars news
    try: 
        browser = init_browser()
        url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
        browser.visit(url)

        time.sleep(1)

        html = browser.html
        soup = BeautifulSoup(html, "html.parser")

        news_title = soup.find("div", class_="content_title").get_text()
        new_p = soup.find("div", class_="rollover_description_inner").get_text()
    
        mars_information["news_title"] = news_title 
        mars_information["news_p"] = new_p

        return mars_information

    finally:   
        browser.quit()

def featured_image():

    try: 
        browser = init_browser()
        url_2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url_2)

        time.sleep(1) 

        html = browser.html
        soup = BeautifulSoup(html, "html.parser")

        image_container = soup.find('div', class_='carousel_items')
        link = image_container.article['style']
        featured_image = link.replace("background-image: url('", "https://www.jpl.nasa.gov").replace("');","")

        mars_information["featured_image_url"] = featured_image

        return mars_information
    
    finally: 
        browser.quit()

def weather():
    
    try: 
        browser = init_browser()
        url_3 = "https://twitter.com/marswxreport?lang=en"
        browser.visit(url_3)

        time.sleep(2)

        html = browser.html
        soup = BeautifulSoup(html, "html.parser")

        weather_results = soup.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
        time.sleep(2)
        
        for weather in weather_results:
            tweet = weather.get_text()
            weather_tweets = []
            if "sol" in tweet:
                weather_tweets.append(tweet)
                time.sleep(1)
        
        mars_weather = weather_tweets[0].replace('\n', ' ').replace('InSight s', 'S')

        mars_information["mars_weather"] = mars_weather

        return mars_information
     
    finally: 
        browser.quit()
    

    #mars facts
def mars_facts():
    
    url_4 = "https://space-facts.com/mars/"
    time.sleep(1)
    tables = pd.read_html(url_4)
    mars_facts_df = tables[1]
    mars_facts_df.rename(columns={0:'Description', 1:'Value'}, inplace=True)
    mars_facts_df.set_index('Description', inplace=True)
    df = mars_facts_df.to_html()

    mars_information["html_mars_facts_df"] = df

        
    
    return mars_information

def mars_hemispher():
    
    url_5 = "https://space-facts.com/mars/"
    time.sleep(1)
    tables = pd.read_html(url_4)
    mars_facts_df = tables[1]
    mars_facts_df.rename(columns={0:'Description', 1:'Value'}, inplace=True)
    mars_facts_df.set_index('Description', inplace=True)
    df = mars_facts_df.to_html()

    mars_information["html_mars_facts_df"] = df

        
    
    return mars_information