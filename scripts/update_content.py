import requests
from bs4 import BeautifulSoup
import json

def fetch_webpage(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def clean_text(text):
    # Replace newline characters with a space and remove escaped quotes, then strip whitespace
    return text.replace("\n", " ").replace('\\"', "").strip()

def parse_tld_table(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find("table", id="tld-table")
    tld_data = {}
    if table:
        tbody = table.find("tbody")
        rows = tbody.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 3:
                # Extract the domain text from the <a> inside the first column (keep the leading dot)
                domain_anchor = cols[0].find("a")
                if domain_anchor and domain_anchor.text:
                    domain_text = clean_text(domain_anchor.text).lower()
                    tld_key = domain_text  # Keep the leading dot
                else:
                    continue

                # Second column: TLD type
                tld_type = clean_text(cols[1].text)

                # Third column: TLD Manager
                tld_manager = clean_text(cols[2].text)

                # Create a dictionary for this TLD with the key "tld type"
                tld_data[tld_key] = {
                    "tld type": tld_type,
                    "tld manager": tld_manager
                }
    return tld_data

def update_json_file(data, file_path="tld_data.json"):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    url = "https://www.iana.org/domains/root/db"
    html = fetch_webpage(url)
    data = parse_tld_table(html)
    update_json_file(data)
    print("JSON file 'tld_data.json' updated successfully.")

if __name__ == '__main__':
    main()
