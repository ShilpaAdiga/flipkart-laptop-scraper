import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import time
import random

def clean_short_name(name):
    name = name.strip()
    if name.endswith("..."):
        # Remove last incomplete word
        name = name[:-3].rstrip()  # remove '...' and trailing space
        if " " in name:
            name = name[:name.rfind(" ")]  # remove until last full word
    return name


# Headers to mimic browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

# Store results
results = []

query = "laptops under 60000"
url = f"https://www.flipkart.com/search?q={query}"

response = requests.get(url, headers=headers)
print("Main Page Status:",response.status_code)

soup = bs(response.text, "html.parser")
product_box = soup.find_all("div", class_="_75nlfW")
print("Products Found:", len(product_box))

for box in product_box:
    name = box.find("div", class_="KzDlHZ")
    f_name = clean_short_name(name.text) if name else "N/A"
    price = box.find("div", class_="Nx9bqj _4b5DiR")
    rating = box.find("div", class_="XQDdHH")
    link = box.find("a", class_="CGtC98")
    product_link = f"https://www.flipkart.com{link['href']}" if link else None

    full_name = "N/A"

    # Fetch full product name from the product page
    if product_link:
        try:
            product_resp = requests.get(product_link, headers=headers)
            #print(product_resp.status_code)
            product_soup = bs(product_resp.text, "html.parser")
            full_name_tag = product_soup.find("span", class_="VU-ZEz") 
            if full_name_tag:
                full_name = full_name_tag.text.strip()
            time.sleep(random.uniform(1,5)) 
        except Exception as e:
            print(f"Error fetching full name: {e}")

    if name and price:
        brand = name.text.strip().split()[0] 
        if full_name == "N/A":
            full_name = f_name

        results.append({
            "Brand": brand,
            "Full Product Name": full_name,
            "Price": price.text.strip(),
            "Rating": rating.text.strip() if rating else "N/A",
            "Link": product_link,
            "Site": "Flipkart"
        })

df = pd.DataFrame(results)
df.to_excel("flipkart_full_data.xlsx", index=False)
print("✅ Full data saved to flipkart_full_data.xlsx")
  
