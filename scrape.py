import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
import time

def scrape_website(website):
    print("Launching edge browser...")

    edge_driver_path ="msedgedriver.exe"
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=Service(edge_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded successfully.")
        html = driver.page_source
        time.sleep(5)


        return html
    
    finally:
        driver.quit()
