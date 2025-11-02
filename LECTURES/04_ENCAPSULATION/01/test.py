import re

email = "pe77er@gmail.com"

pattern = r'([A-Za-z0-9]+)@([A-Za-z]+)\.([A-Za-z]+)'
match = re.match(pattern,email)

