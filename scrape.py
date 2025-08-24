import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from bs4 import BeautifulSoup
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
        return html
    
    finally:
        driver.quit()

def extract_body_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.body
    return str(body) if body else "No body content found."

def clean_body_content(body):
    soup = BeautifulSoup(body, 'html.parser')

    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()
    
    cleaned_content = soup.get_text(separator='\n')
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())   # Remove empty lines

    return cleaned_content

def split_dom_content(dom_content, chunk_size=6000):
    return [dom_content[i:i + chunk_size] for i in range(0, len(dom_content), chunk_size)]


