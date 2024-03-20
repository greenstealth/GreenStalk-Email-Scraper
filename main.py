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
    print("Insira o termo de busca para a raspagem de e-mails usando Google Dorks.")
    print("Exemplo: 'site:br contato@', 'site:com gmail.com'")
    query = input("Digite o termo de busca: ")
    return query

def main():
    print_banner()
    query = main_menu()
    output_file = "emails.csv"
    scraper = EmailScraper(query)
    scraper.run(output_file)

if __name__ == "__main__":
    main()
