from email_scraper import EmailScraper
from email_filter import filter_emails
from email_saver import save_emails_to_csv

def print_banner():
    banner = """
    ██████╗ ███████╗███████╗██████╗ ███╗   ██╗████████╗ █████╗ ██╗  ██╗███████╗
    ██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║╚══██╔══╝██╔══██╗██║ ██╔╝██╔════╝
    ██████╔╝█████╗  █████╗  ██████╔╝██╔██╗ ██║   ██║   ███████║█████╔╝ █████╗  
    ██╔═══╝ ██╔══╝  ██╔══╝  ██╔══██╗██║╚██╗██║   ██║   ██╔══██║██╔═██╗ ██╔══╝  
    ██║     ███████╗███████╗██║  ██║██║ ╚████║   ██║   ██║  ██║██║  ██╗███████╗
    ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
    """
    print(f"\033[92m{banner}\033[0m")  # 92 é o código para a cor verde no terminal

def main_menu():
    print("1. Raspagem de e-mails brasileiros")
    print("2. Raspagem de e-mails do Gmail")
    print("3. Raspagem de e-mails em massa de arquivo de URLs")
    choice = input("Escolha uma opção: ")
    return choice

def main():
    print_banner()
    choice = main_menu()
    if choice == '3':
        urls_file = input("Digite o caminho do arquivo com as URLs: ")
        output_file = input("Digite o nome do arquivo de saída para os e-mails: ")
        scraper = EmailScraper(urls_file)
        scraper.run(output_file)
    else:
        url = input("Digite a URL para fazer o scraping de e-mails: ")
        scraper = EmailScraper(url)
        emails = scraper.scrape_emails_from_url(url)
        if choice == '1':
            filtered_emails = filter_emails(emails, '.br')
        elif choice == '2':
            filtered_emails = filter_emails(emails, 'gmail.com')
        save_emails_to_csv(filtered_emails, f'emails_{choice}.csv')

if __name__ == "__main__":
    main()
