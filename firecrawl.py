from firecrawl import FirecrawlApp
import requests
from bs4 import BeautifulSoup

def scrape_promotions_from_firecrawl(url):
    # Initialize FirecrawlApp
    firecrawl = FirecrawlApp(api_key="fc-7eed36a9aaa84e3faba138d6c6d5bd16")
    
    # Scrape the URL and get the page content
    page_content = firecrawl.scrape_url(
        url=url,
        params={"pageOptions": {"onlyMainContent": True}}  # Ignore navs, footers, etc.
    )
    
    return page_content

def scrape_promotions_from_html(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all elements with class "promotions-list-item" or "promotion-item"
    promotions = soup.find_all("div", class_=["promotions-list-item", "promotion-item"])
    print("Scraping promotions from:", url)

    # Extract promotion information
    for promotion in promotions:
        # Extract promotion text
        promotion_text = promotion.text.strip()

        # Extract promotion title
        promotion_title = promotion.find("div", class_="promotion-title") or promotion.find("h3", class_="promotion-title")
        if promotion_title:
            promotion_title_text = promotion_title.text.strip()
            print()
            print("Promotion Title:", promotion_title_text)

        # Print promotion text
        print("Promotion Text:", promotion_text)
    
    # Print an empty line between promotions from different URLs
    print()

# URL to scrape using Firecrawl
firecrawl_url = "https://www.winchesterequipment.com/regional-promotions"
firecrawl_page_content = scrape_promotions_from_firecrawl(firecrawl_url)
print("Firecrawl page content:")
print(firecrawl_page_content)
print()

# URL to scrape using requests and BeautifulSoup
html_url = "https://www.winchesterequipment.com/regional-promotions"
scrape_promotions_from_html(html_url)
