import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def parse_elements(html, tag, class_name=None):
    soup = BeautifulSoup(html, 'html.parser')
    elements = []

    # Select elements based on tag and optional class
    if class_name:
        items = soup.find_all(tag, class_=class_name)
    else:
        items = soup.find_all(tag)

    for item in items:
        elements.append(item.get_text(strip=True))

    return elements

def display_elements(elements, tag, class_name):
    if elements:
        print(f"\nContent found for tag '{tag}'" + (f" with class '{class_name}'" if class_name else "") + ":")
        for i, element in enumerate(elements, 1):
            print(f"{i}. {element}")
    else:
        print("No content found with the specified tag and class.")

def main():
    url = input("Enter the URL of the website: ")
    tag = input("Enter the HTML tag you want to scrape. This step is required. (e.g., h1, p, div): ")
    class_name = input("Enter the class name to filter by (optional, press Enter to skip): ")

    html = fetch_page(url)
    if html:
        elements = parse_elements(html, tag, class_name if class_name else None)
        display_elements(elements, tag, class_name)

if __name__ == "__main__":
    main()
