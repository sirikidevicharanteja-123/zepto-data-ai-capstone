#import required libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pathlib import Path

def scrape_books():
  #create empty lists to append scraped data 
  titles=[]
  prices=[]
  star_ratings=[]
  availabilitys=[]
  categories=[]

  #URLs of Different Book Categories
  urls=["http://books.toscrape.com/catalogue/category/books/travel_2/index.html","https://books.toscrape.com/catalogue/category/books/mystery_3/index.html","https://books.toscrape.com/catalogue/category/books/fiction_10/index.html","https://books.toscrape.com/catalogue/category/books/science_22/index.html","https://books.toscrape.com/catalogue/category/books/horror_31/index.html"]

  #Limit of books for each Category
  limit= 16

  #Loop through Each category URL
  for url in urls:
      #send to web page
      web=requests.get(url)
      #Parse to html content
      soup=BeautifulSoup(web.content,'html.parser')

      #Extract The category
      category = soup.find("div", class_="page-header action").find("h1").get_text(strip=True)
      
      #Find all book containers on the page
      result=soup.find_all('article',class_='product_pod')

      #Loop through Each container(book) upto to certain limit
      for res in result[:limit]:

            # Extract and store book title
            title = res.find('h3').find('a')['title']
            titles.append(title)

            # Extract and store book price
            price = res.find('p',class_='price_color').get_text(strip=True)
            prices.append(price)

            # Extract and store star rating
            star_rating = res.find('p',class_='star-rating')["class"][1]
            star_ratings.append(star_rating)

            # Extract and store availability status
            availability = res.find('p',class_="instock availability").get_text(strip=True)
            availabilitys.append(availability)

            # Add the category for the current book
            categories.append(category)
  #Creating a pandas DataFrame from the scraped data
  df=pd.DataFrame({
      "title":titles,
      "price":prices,
      "star_rating":star_ratings,
      "availability":availabilitys,
      "category":categories
  })

  #Display thr full titles of the book
  pd.set_option('display.max_colwidth', None)
  
  return df
def main():
  df=scrape_books()
  
  # Get project paths
  base_dir = Path(__file__).resolve().parent
  output_path = base_dir / "data" / "raw_data.csv"
  
  # Display results
  print("\nScraping completed successfully!")
  print(f"Total books scraped: {len(df)}")
  
  print("\nData preview: \n")
  print(df.head())
  
  print(f"\nData path :{output_path}")

if __name__=="__main__":
  main()  