# Flipkart Laptop Price Scraper 🖥️📊

This Python project scrapes laptops under ₹60,000 from [Flipkart](https://www.flipkart.com) using `requests` and `BeautifulSoup`.

It collects:
- Laptop Brand
- Full Product Name
- Price
- Rating
- Product Link

The data is cleaned and saved into an Excel file (`flipkart_full_data.xlsx`), which is ready for analysis or business use.

---

## 🔧 Tools Used

- **Python**
- **BeautifulSoup** – HTML parsing
- **Pandas** – Data structuring and Excel export
- **Requests** – HTTP requests
- **OpenPyXL** – Excel file writing

---

## 📄 Features

- Scrapes main listing page and optionally fetches full product name from each product page
- Handles truncated product names (ending with `...`)
- Adds delay to avoid rate-limiting (HTTP 429)
- Cleans and exports data to Excel

---

## 📁 Sample Output

| Brand  | Product Name | Price | Rating |
|--------|--------------|-------|--------|
| HP     | HP Pavilion Ryzen 5... | ₹57,990 | 4.2 |
| ASUS   | ASUS Vivobook 15...    | ₹58,490 | 4.3 |

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python flipkart_scraper.py
