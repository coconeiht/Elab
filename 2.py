class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.__min_length = min_length
        self.__mails = mails
        self.__domains = domains

    def __validate_name(self, name):
        return len(name) >= self.__min_length

    def __validate_mail(self, mail):
        return mail in self.__mails

    def __validate_domain(self, domain):
        return domain in self.__domains

    def validate(self, email):
        try:
            name, rest = email.split('@')
            mail, domain = rest.split('.')
        except ValueError:
            return False
        
        # Use the three private methods
        return self.__validate_name(name) and self.__validate_mail(mail) and self.__validate_domain(domain)
