import csv

def save_emails_to_csv(emails, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for email in emails:
            writer.writerow([email])
    print(f"E-mails salvos com sucesso em {filename}")
