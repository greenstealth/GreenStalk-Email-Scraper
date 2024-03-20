import requests
from bs4 import BeautifulSoup
import re
import time
import urllib.parse

class EmailScraper:
    def __init__(self, query, max_results=100):
        self.query = query
        self.max_results = max_results
        self.email_regex = re.compile(r'([a-zA-Z0-9_.+]+@[a-zA-Z0-9_.+]+)', re.VERBOSE)

    def google_search(self):
        headers = {'User-Agent': 'Mozilla/5.0'}
        urls = []

        query_encoded = urllib.parse.quote_plus(self.query)
        for start in range(0, self.max_results, 10):
            search_url = f"https://www.google.com/search?q={query_encoded}&start={start}"
            response = requests.get(search_url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                for link in soup.find_all('a', href=True):
                    href = link.get('href')
                    if '/url?q=' in href:
                        actual_url = href.split('/url?q=')[1].split('&')[0]
                        if actual_url.startswith('http'):
                            urls.append(urllib.parse.unquote(actual_url))
            else:
                print(f"Erro {response.status_code} ao acessar {search_url}")

            time.sleep(1)  # Be respectful to Google's servers

        return urls

    def scrape_emails_from_url(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                emails = set(self.email_regex.findall(response.text))
                return emails
            else:
                print(f"Erro ao acessar {url}: {response.status_code}")
                return set()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {url}: {e}")
            return set()

    def run(self, output_file):
        with open(output_file, 'a') as email_file:
            urls = self.google_search()
            processed_urls = set()
            
            for url in urls:
                if url not in processed_urls:
                    emails = self.scrape_emails_from_url(url)
                    for email in emails:
                        email_file.write(f"{email}\n")
                    processed_urls.add(url)
                    print(f"Processed {url} with {len(emails)} emails found.")
import requests
from bs4 import BeautifulSoup
import re
import time
import urllib.parse

class EmailScraper:
    def __init__(self, query, max_results=100):
        self.query = query
        self.max_results = max_results
        self.email_regex = re.compile(r'([a-zA-Z0-9_.+]+@[a-zA-Z0-9_.+]+)', re.VERBOSE)

    def google_search(self):
        headers = {'User-Agent': 'Mozilla/5.0'}
        urls = []

        query_encoded = urllib.parse.quote_plus(self.query)
        for start in range(0, self.max_results, 10):
            search_url = f"https://www.google.com/search?q={query_encoded}&start={start}"
            response = requests.get(search_url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                for link in soup.find_all('a', href=True):
                    href = link.get('href')
                    if '/url?q=' in href:
                        actual_url = href.split('/url?q=')[1].split('&')[0]
                        if actual_url.startswith('http'):
                            urls.append(urllib.parse.unquote(actual_url))
            else:
                print(f"Erro {response.status_code} ao acessar {search_url}")

            time.sleep(1)  # Be respectful to Google's servers

        return urls

    def scrape_emails_from_url(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                emails = set(self.email_regex.findall(response.text))
                return emails
            else:
                print(f"Erro ao acessar {url}: {response.status_code}")
                return set()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {url}: {e}")
            return set()

    def run(self, output_file):
        with open(output_file, 'a') as email_file:
            urls = self.google_search()
            processed_urls = set()
            
            for url in urls:
                if url not in processed_urls:
                    emails = self.scrape_emails_from_url(url)
                    for email in emails:
                        email_file.write(f"{email}\n")
                    processed_urls.add(url)
                    print(f"Processed {url} with {len(emails)} emails found.")
