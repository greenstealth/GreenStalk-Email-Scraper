def filter_emails(emails, domain):
    # Esta função agora pode ser expandida para incluir lógica mais complexa se necessário.
    if domain == '.br':
        return {email for email in emails if email.endswith('.br') or 'brasil' in email or 'brazil' in email}
    else:
        return {email for email in emails if email.endswith(domain)}
