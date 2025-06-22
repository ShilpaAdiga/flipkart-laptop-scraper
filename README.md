# Flipkart Laptop Price Scraper 🖥️📊

Python script to scrape laptop listings under ₹60,000 from **Flipkart** using `requests` and `BeautifulSoup`, clean product data, and export it to Excel.

---

## ✅ Features

- Scrapes **Brand**, **Product Name**, **Price**, **Rating**, and **Product Link**  
- Visits individual product pages to retrieve the **full title** (fallback to cleaned short title if blocked)  
- Implements **delay handling** to avoid HTTP 429 rate limits  
- Exports structured data to **flipkart_full_data.xlsx**

---

## 🛠️ Tech Stack

- **Python**  
- **BeautifulSoup** (HTML parsing)  
- **Requests** (HTTP operations)  
- **pandas** (data manipulation + Excel export)  
- **openpyxl** (Excel writer)

---

## 📊 Sample Output

| Brand | Product Name                          | Price   | Rating |
|-------|---------------------------------------|---------|--------|
| HP    | HP Pavilion Ryzen 5 …                | ₹57,990 | 4.2    |
| ASUS  | ASUS Vivobook 15 …                   | ₹58,490 | 4.3    |

---

## 🚀 Quickstart

```bash
# 1. Clone the repository
git clone https://github.com/ShilpaAdiga/flipkart-laptop-scraper.git
cd flipkart-laptop-scraper

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the scraper
python flipkart_scraper.py


## 💡 Next Steps

- Expand scrape to **other price ranges/categories**  
- Add **data analysis or visualization** (e.g., price distribution, brand comparison)  
- Integrate into a **dashboard** or **web app** using Streamlit or Flask
