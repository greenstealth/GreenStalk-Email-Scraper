def filter_emails(emails, domain):
    return {email for email in emails if email.endswith(domain)}
