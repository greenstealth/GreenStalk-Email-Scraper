import requests
from bs4 import BeautifulSoup
import re
import time

class EmailScraper:
    def __init__(self, query, max_results=100):
        self.query = query
        self.max_results = max_results
        self.email_regex = re.compile(r'([a-zA-Z0-9_.+]+@[a-zA-Z0-9_.+]+)', re.VERBOSE)

    def google_search(self):
        headers = {'User-Agent': 'Mozilla/5.0'}
        urls = []
        for start in range(0, self.max_results, 10):
            url = f"https://www.google.com/search?q={self.query}&start={start}"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                if href.startswith('/url?q='):
                    actual_url = href.split('&')[0].replace('/url?q=', '')
                    urls.append(actual_url)
            time.sleep(1)  # Be respectful to Google's servers
        return urls

    def scrape_emails_from_url(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers)
            emails = set(self.email_regex.findall(response.text))
            return emails
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {url}: {e}")
            return set()

    def run(self, output_file):
        with open(output_file, 'a') as email_file:
            urls = self.google_search()
            for i, url in enumerate(urls, 1):
                emails = self.scrape_emails_from_url(url)
                for email in emails:
                    email_file.write(f"{email}\n")
                print(f"{i}. Processed {url} with {len(emails)} emails found.")

# Uso da classe
# query = 'site:br "contato@"'
# scraper = EmailScraper(query)
# scraper.run('emails.txt')
