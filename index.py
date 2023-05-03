from playwright.sync_api import Playwright, sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    product_url = "https://www.flipkart.com/yonex-nanoray-light-18i-black-strung-badminton-racquet-weight-77-g-tension-30-lbs/p/itm441bf79a97749?pid=RAQF2X6EWUGZBYVH&lid=LSTRAQF2X6EWUGZBYVHMMNMAG&marketplace=FLIPKART&store=abc%2Fegs&srno=b_1_7&otracker=browse&fm=search-autosuggest&iid=94be2b17-3db2-49f3-a0fd-c4a1c2a87fab.RAQF2X6EWUGZBYVH.SEARCH&ppt=browse&ppn=browse&ssid=lxp518tadc0000001683108996398"
    page = context.new_page()
    page.goto(product_url)
    product_name = page.wait_for_selector('span[class="B_NuCI"]',timeout=120000).inner_text()
    product_url = page.url
   
   
    price = page.wait_for_selector('div[class="_30jeq3 _16Jk6d"]').inner_text()
    price = price.replace('\u20b9', 'INR ')
    

   

    print("Product Name: ", product_name)
    print("Product URL: ", product_url)
   
    print("Price: ", price)
    
    context.close()
    browser.close()



