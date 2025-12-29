# bookmeter-wishlist-scraper

A lightweight Python web scraper that extracts all books from a specific user's **読みたい本** on [読書メーター](https://bookmeter.com/).

It handles pagination automatically, crawling through all pages to retrieve the complete list of book titles and their authors.

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/your-username/bookmeter-wishlist-scraper.git
cd bookmeter-wishlist-scraper

```


2. **Install dependencies**:
This project uses `requests` for fetching pages and `BeautifulSoup4` for parsing HTML.
```bash
pip install requests beautifulsoup4

```

Windows(powershell)
```powershell
python -m pip install requests beautifulsoup4
```



## Usage

1. Open `bookmeter-wishlist-scraper.py`.
2. Replace the `USER_ID` variable with the target Bookmeter user ID.
```python
USER_ID = "1000000000" # Example User ID

```


3. Run the script:
```bash
python bookmeter-wishlist-scraper.py

```



## Output Example

The script will output the results to your terminal as follows:

```text
--- Scraping Results ---
1. [佐藤 正午] 熟柿
2. [五条 紀夫] 殺人事件に巻き込まれて走っている場合ではない…
3. [塩田 武士] 踊りつかれて
4. [フリーダ・マクファデン] ハウスメイド (ハヤカワ・ミステリ文庫)
5. [夕木 春央] 十戒 (講談社文庫 ゆ 10-4)
```

## Requirements

* Python 3.6+
* requests
* beautifulsoup4

## Note

This tool is for personal use. Please ensure you comply with Bookmeter's [Terms of Service](https://bookmeter.com/terms) and robots.txt policies when using scrapers.

## License

[MIT License](https://www.google.com/search?q=LICENSE)