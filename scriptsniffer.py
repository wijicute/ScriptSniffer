import requests
import re
from urllib.parse import urlparse, urljoin

print("""\033[33m

.d8888.  .o88b. d8888b. d888888b d8888b. d888888b        .d8888. d8b   db d888888b d88888b d88888b d88888b d8888b. 
88'  YP d8P  Y8 88  `8D   `88'   88  `8D `~~88~~'        88'  YP 888o  88   `88'   88'     88'     88'     88  `8D 
`8bo.   8P      88oobY'    88    88oodD'    88           `8bo.   88V8o 88    88    88ooo   88ooo   88ooooo 88oobY' 
  `Y8b. 8b      88`8b      88    88~~~      88    C8888D   `Y8b. 88 V8o88    88    88~~~   88~~~   88~~~~~ 88`8b   
db   8D Y8b  d8 88 `88.   .88.   88         88           db   8D 88  V888   .88.   88      88      88.     88 `88. 
`8888Y'  `Y88P' 88   YD Y888888P 88         YP           `8888Y' VP   V8P Y888888P YP      YP      Y88888P 88   YD 
\033[37m
This tool assists you in identifying all paths (URLs) that start with a / from an online JavaScript file.
It then converts these paths into complete (absolute) links and saves them in a text file named after the website's domain.
[\033[32m+\033[37m] Developers: Erfan Nouri - Amin Shahbazi            [\033[32m+\033[37m] Telegram: @Er4vnn - @RozeSec
[\033[32m+\033[37m] Github: https://github.com/RozeSec                 [\033[32m+\033[37m] Version: 1.0      
""")

def extract_relative_links(js_url):
    try:
        response = requests.get(js_url)
        response.raise_for_status()
        js_content = response.text
    except requests.RequestException as e:
        print(f"Error fetching the JavaScript file: {e}")
        return [], None

    # Parse the base URL and derive output filename from domain
    parsed = urlparse(js_url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    output_filename = f"{parsed.netloc}.txt"

    # Regex to find strings starting with '/'
    pattern = r'(?:"|\')(/[^"\']+)(?:"|\')'
    matches = re.findall(pattern, js_content)

    # Remove duplicates and build absolute URLs
    seen = set()
    links = []
    for rel in matches:
        if rel not in seen:
            seen.add(rel)
            full_url = urljoin(base_url, rel)
            links.append(full_url)

    return links, output_filename

if __name__ == "__main__":
    js_url = input("\033[37mEnter the JavaScript file URL: ").strip()
    links, filename = extract_relative_links(js_url)

    if links:
        print("\nExtracted absolute URLs:")
        for link in links:
            print(link)
        # Save to domain-based filename
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for link in links:
                    f.write(link + "\n")
            print(f"\nLinks have been saved to {filename}")
        except IOError as e:
            print(f"Error writing to file {filename}: {e}")
    else:
        print("No relative URLs found or an error occurred.")
