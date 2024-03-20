import csv
import os

def save_emails_to_csv(emails, filename):
    mode = 'a' if os.path.exists(filename) else 'w'
    # Remover duplicatas convertendo a lista para um conjunto
    unique_emails = set(emails)

    with open(filename, mode=mode, newline='') as file:
        writer = csv.writer(file)
        for email in sorted(unique_emails):  # Ordenar os e-mails alfabeticamente
            writer.writerow([email])

    print(f"E-mails salvos com sucesso em {filename}")
