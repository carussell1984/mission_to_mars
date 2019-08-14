# Mission to Mars - Web Scraping

<img src="mars-surface_img.jpg" alt="">

<div>
 <h3>Project Overview:</h3
 <p>The objective was to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.</p>
</div>

<div>
 <h3>Step 1 - Use Jupyter Notebook to write the code to scrape Data for the following Items:</h3
   <ul>
  <li>Find the latest new and news summary: https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest</li>
  <li>Find the featured Mars photo: https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars</li>
  <li>Retrive the latest weather information via tweet: https://twitter.com/marswxreport?lang=en</li>
  <li>Find facts on mars using Pandas: https://space-facts.com/mars/</li>
  <li>Find high resolution pictures of Mar's hemisphere: https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars </li>
  </ul>
</div>
<div>
  <h3>Step 2 Use MongoDB with FLask to create an HTML page that displays all the information from the URLs above:</h3>
  <p>
  The Jupyter notebook was converted into a Python script entitled <code>scrape_mars.py</code>, and has a function called <code>scrape</code> that performs all the scraping. A route called <code>/scrape</code> was created to import scrape_mars.py script and calls the scrape function. A route called <code>/</code> was created that will queries the Mongo database and passes the mars data into an HTML template to display the data. Lastly an HTML file was created that will take the mars data dictionary and display all the data in the appropriate HTML elements. 
  </p>
 
 <div>
  <h3>Resources</h3>
   <ul>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  </ul>
  
