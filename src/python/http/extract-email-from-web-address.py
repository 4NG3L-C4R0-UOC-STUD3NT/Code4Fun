import re
import requests

url = "https://www.pythonpool.com/contact-us"

EMAIL_REGEX = r"[\w\.-]+@[\w\.-]+"

r = requests.get(url)

print("Emails: ")
print("***********************")

for re_match in re.findall(EMAIL_REGEX, r.text):
    print(re_match)

