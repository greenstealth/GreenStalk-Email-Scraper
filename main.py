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
    print("1. Raspagem de e-mails brasileiros usando Google Dorks")
    print("2. Raspagem de e-mails do Gmail usando Google Dorks")
    choice = input("Escolha uma opção: ")
    return choice

def main():
    print_banner()
    choice = main_menu()
    output_file = "emails.csv"

    if choice == '1':
        query = 'site:br "contato@"'
        scraper = EmailScraper(query)
        scraper.run(output_file)
        emails = scraper.scrape_emails_from_url(query)  # Esta linha não é mais necessária
    elif choice == '2':
        query = 'site:com "gmail.com"'
        scraper = EmailScraper(query)
        scraper.run(output_file)
        emails = scraper.scrape_emails_from_url(query)  # Esta linha não é mais necessária

    # Aqui, você poderia adicionar a lógica para filtrar e salvar os e-mails, se necessário.

if __name__ == "__main__":
    main()
