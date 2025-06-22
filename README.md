# Flipkart Laptop Price Scraper 🖥️📊

This Python project scrapes laptop listings under ₹60,000 from [Flipkart](https://www.flipkart.com) using `requests` and `BeautifulSoup`, then cleans and exports the data to Excel.

## ✅ Features

- Scrapes brand, full product name, price, rating, and link
- Visits product pages to get the full name (with fallback cleaning if blocked)
- Handles 429 errors using time delay
- Exports cleaned data to `flipkart_full_data.xlsx`

## 📊 Sample Output

| Brand | Product Name | Price | Rating |
|-------|--------------|-------|--------|
| HP    | HP Pavilion Ryzen 5 ... | ₹57,990 | 4.2 |
| ASUS  | ASUS Vivobook 15 ...    | ₹58,490 | 4.3 |

## 🛠️ Tools Used

- Python
- BeautifulSoup
- Requests
- pandas
- openpyxl

## 🚀 How to Run

1. Clone the repo  
2. Install dependencies:

```bash
pip install -r requirements.txt
