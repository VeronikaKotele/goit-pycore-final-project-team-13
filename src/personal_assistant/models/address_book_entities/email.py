import re

class Email:
    def __init__(self, value):
        # Email format: local-part@domain.tld
        email_pattern = re.compile(
            r'^'
            r'[a-zA-Z0-9._%+-]+'               # local part before @: alphanumeric and ._%+- characters
            r'@'                               # @ symbol
            r'[a-zA-Z0-9]+[a-zA-Z0-9.-]+'      # domain name: alphanumeric and .- characters, but not starting with dot
            r'\.'                              # dot before TLD (top-level domain)
            r'[a-zA-Z]{2,}'                    # TLD: at least 2 alphabetic characters
            r'$'
        )
        if not email_pattern.match(value):
            raise ValueError(f"Invalid email format: {value}")
        self.value = value

    def __str__(self):
        return str(self.value)
