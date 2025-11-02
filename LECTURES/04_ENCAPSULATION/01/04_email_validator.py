import re

class EmailValidator:
    def __init__(self,min_length,mails_ :list,domains_ :list):
        self.min_length = min_length
        self.mails = mails_
        self.domains = domains_

    def __is_name_valid(self,name :str) -> bool:

        is_wth_proper_length = (len(name) >= self.min_length)
        return is_wth_proper_length

    def __is_mail_valid(self,mail):
        is_valid_mail = any(mail == m for m in self.mails)
        return is_valid_mail

    def __is_domain_valid(self,domain):
        is_valid_domain = any(domain == d for d in self.domains)
        return is_valid_domain

    def validate(self,email):
        pattern = r'([A-Za-z0-9]+)@([A-Za-z]+)\.([A-Za-z]+)'
        match = re.match(pattern, email)
        name = match.group(1)
        mail = match.group(2)
        domain = match.group(3)


        is_valid = (self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain))

        return is_valid

mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))