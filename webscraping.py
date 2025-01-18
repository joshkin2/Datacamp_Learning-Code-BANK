#requests
import requests
url = 'https://www.sample.com/'
r = requests.get(url)
r.status_code : 200
#WEB SCRAPING 
#import Beautiful Soup to parse the web page content EG
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
# Specify the URL of the webpage you want to scrape
url = 'https://en.wikipedia.org/wiki/IBM'
# Send an HTTP GET request to the webpage
response = requests.get(url)
# Store the HTML content in a variable
html_content = response.text
# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')
# Display a snippet of the HTML content EG
print(html_content[:500])
#pandas read_html for table extraction
read_html()

#extracting tables from webpages
import pandas as pd
URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
tables = pd.read_html(URL)
df = tables[0]   or use df = tables(2)     #required table will have index 2
print(df)

#SAMPLE OF WEBSCRAPING
#to perform webscraping we need to install these libraries with the codes
!mamba install bs4==4.10.0 -y
!pip install lxml==4.6.4
!mamba install html5lib==1.1 -y
!pip install requests==2.26.0
import requests
from bs4 import BeautifulSoup
page = requests.get('http://EnterWebsiteURL'...).text
#creates a BeautifulSoup object   EG
soup = BeautifulSoup(page, 'html.parser')
#pulls all instances of <a> tag
artists = soup.find_all('a')
#clears data of all tags
for artist in artists:
    names = artist.contents[0]
    fullLink = artist.get('href')
    print(names)
    print(fullLink)

#parse html through BS constructor
soup = BeautifulSoup(html, 'html.parser')
#display html in nested structure
print(soup.prettify())

#Downloading And Scraping The Contents Of A Web Page
url = 'http://www.ibm.com'
#We use get to download the contents of the webpage in text format and store in a variable called data   EG
data = requests.get(url).text

#We create a BeautifulSoup object using the BeautifulSoup constructor
soup = BeautifulSoup(data.'html.parser')
#Scrape all links
for link in soup.find_all('a' .href=True):
    print(link.get('href'))     # in html anchor/link is represented by the tag <a>
#Scrape all images Tags
for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))    

#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
#Before proceeding to scrape a web site, you need to examine the contents, and the way data is organized on the website. Open the above url in your browser and check how many rows and columns are there in the color table.
#get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")
#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>
#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))

#Scrape data from HTML tables into a DataFrame using BeautifulSoup and Pandas
import pandas as pd
#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"
Before proceeding to scrape a web site, you need to examine the contents, and the way data is organized on the website. Open the above url in your browser and check the tables on the webpage.
# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")
#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>
# we can see how many tables were found by checking the length of the tables list
len(tables)
#Assume that we are looking for the 10 most densly populated countries table, we can look through the tables list and find the right one we are look for based on the data in each table or we can search for the table name if it is in the table but this option might not always work.
for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)
#See if you can locate the table name of the table, 10 most densly populated countries, below.
print(tables[table_index].prettify())
population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])
​for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)
​population_data
#Scrape data from HTML tables into a DataFrame using BeautifulSoup and read_html
#Using the same url, data, soup, and tables object as in the last section we can use the read_html function to create a DataFrame.
#Remember the table we need is located in tables[table_index]
#We can now use the pandas function read_html and give it the string version of the table as well as the flavor which is the parsing engine bs4.
pd.read_html(str(tables[5]), flavor='bs4')
#The function read_html always returns a list of DataFrames so we must pick the one we want out of the list.
population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]
​population_data_read_html
#Scrape data from HTML tables into a DataFrame using read_html
#We can also use the read_html function to directly get DataFrames from a url.
dataframe_list = pd.read_html(url, flavor='bs4')
#We can see there are 25 DataFrames just like when we used find_all on the soup object.
len(dataframe_list)
#Finally we can pick the DataFrame we need out of the list.
dataframe_list[5]
#We can also use the match parameter to select the specific table we want. If the table contains a string matching the text it will be read.
pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]

#download historical stock prices using yfinance
import yfinance as yf
#download historical data for a stock    EG
msft = yf.Ticker('MSFT')      #AKA microsoft
msft_data = msft.history(period='max')
#display the downloaded data
msft_data.head()
country = usa
sector = technology

#Steps for extracting the data from webpage using web scraping
#1:  send http request to web page
url = 'https://sample.html'
data = requests.get(url).text
print(data)
#2:  Parse the HTML content with BeautifulSoup library
soup = BeautifulSoup(data, 'html5lib')
#3:  Identify HTML tags and covert table in webpage to DF
netflix_data = pd.DataFrame(columns=['Date','Open', 'High', 'Low', 'Close', 'Volume'])
#4:  Use a BeautifulSoup method for extracting data
# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    
#    Print the extracted data
netflix_data.head()

#Steps for Extracting data using pandas library
#1:
read_html_pandas_data = pd.read_html(url)
# or convert the BeautifulSoup object to a string
read_html_pandas_data = pd.read_html(str(soup))
#since it's just one table in the page we're using 0 but if it was another table we'd use the specific number
netflix_dataframe = read_html_pandas_data[0]
netflix_dataframe.head()
# print last row of DF
last_row = amazon.data.tail(1)
print(last_rows)
# reset index
netflix_data.reset_index(inplace=True)
#print 2D numpy array values
print(variablename.values)
#print index of columns: col names
print(variablename.columns)
#print index for the rows:row numbers or names
print(variablename.index)

#reading XML files
import pandas as pd
import xml.etree.ElementTree as etree
tree = etree.parse('fileExample.xml')
root = tree.getroot()
columns = ['Name', 'Phone Number', 'Birthday']
df = pd.DataFrame(columns = columns)
for node in root:
    name = node.find('name').text
    phonenumber = node.find('phonenumber').text
    birthday = nod.find('birthday').text
    df = df.append(pd.Series([name, phonenumber, birthday],
    index = columns)....., ignore_index = True





