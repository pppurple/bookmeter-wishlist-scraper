import requests
from bs4 import BeautifulSoup
import time

def scrape_bookmeter_wishlist(user_id):
    base_url = f"https://bookmeter.com/users/{user_id}/books/wish"
    page = 1
    book_list = []
    
    # Set User-Agent to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print(f"Fetching wishlist for User ID: {user_id}...")

    while True:
        # Generate URL for pagination
        url = f"{base_url}?page={page}"
        print(f"Parsing page {page}...")
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status() # Raise an exception for HTTP errors
            
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Locate book detail containers within the grid layout
            book_details = soup.select(".book-list--grid .book__detail")
            
            # If no books are found, assume it's the end of the list and break the loop
            if not book_details:
                print("Reached the end of the wishlist.")
                break
            
            for detail in book_details:
                # Extract author and title from the book detail block
                author_elem = detail.select_one(".detail__authors")
                title_elem = detail.select_one(".detail__title")
                
                if author_elem and title_elem:
                    author = author_elem.get_text(strip=True)
                    title = title_elem.get_text(strip=True)
                    book_list.append({"author": author, "title": title})
            
            # Wait for 1 second to be polite to the server (scraping etiquette)
            time.sleep(1)
            page += 1

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    return book_list

if __name__ == "__main__":
    # Target User ID
    USER_ID = "xxxxx"
    results = scrape_bookmeter_wishlist(USER_ID)

    print("\n--- Scraping Results ---")
    for i, book in enumerate(results, 1):
        print(f"{i}. [{book['author']}] {book['title']}")