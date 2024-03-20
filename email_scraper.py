import requests
from bs4 import BeautifulSoup
import re
import time

class EmailScraper:
    def __init__(self, urls_file):
        self.urls_file = urls_file
        self.email_regex = re.compile(r'''
            ([a-zA-Z0-9_.+]+
            @
            [a-zA-Z0-9_.+]+)
            ''', re.VERBOSE)

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
        with open(self.urls_file, 'r') as urls, open(output_file, 'a') as email_file:
            for i, url in enumerate(urls, 1):
                url = url.strip()
                emails = self.scrape_emails_from_url(url)
                for email in emails:
                    email_file.write(f"{email}\n")
                print(f"{i}. Processed {url} with {len(emails)} emails found.")

# Uso da classe
# scraper = EmailScraper('urls.txt')
# scraper.run('emails.txt')
