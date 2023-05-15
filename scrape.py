import sys
from playwright.sync_api import sync_playwright

def scrape_flipkart_products(url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        page.wait_for_load_state('networkidle')
        
        # Customize the CSS selectors below based on the structure of the Flipkart page
        product_titles = page.query_selector_all('.s1Q9rs')
        product_prices = page.query_selector_all('._25b18c')
       # product_descriptions = page.query_selector_all('.IRpwTa')
        #product_rating=page.query_selector_all('._3LWZlK')
        
        products = []
        
        for i in range(len(product_titles)):
            title = product_titles[i].inner_text()
            rating=product_rating[i].inner_text()
            
            # Check if the product prices list has an element at index i
            if i < len(product_prices):
                price = product_prices[i].inner_text()
            else:
                price = "N/A"  # Set a default value if price is not available
            
            
            

            # Check if the product descriptions list has an element at index i
           # if i < len(product_descriptions):
              #  description = product_descriptions[i].inner_text()
            #else:
                #description = "N/A"  # Set a default value if description is not available
            
            product = {
                'title': title,
                'price': price,
                'rating':rating
               
            }
            
            products.append(product)
        
        context.close()
        browser.close()
        
        return products

# Specify the URL of the Flipkart page you want to scrape
flipkart_url = 'https://www.flipkart.com/sports/cricket/pr?sid=abc,5lf&p[]=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&otracker=nmenu_sub_Sports%2C%20Books%20%26%20More_0_Cricket'

# Call the function to scrape the product details
product_details = scrape_flipkart_products(flipkart_url)

# Display the scraped product details
for product in product_details:
    print("Title:", product['title'])
    sys.stdout.buffer.write("Price: ".encode('utf-8'))
    sys.stdout.buffer.write(product['price'].encode('utf-8'))
    #print("Rating:", product['rating'])
    print()
     