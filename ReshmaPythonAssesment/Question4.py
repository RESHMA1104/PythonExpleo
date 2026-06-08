import re
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
text_emails = "trainer@smartcliff.in"
emails_found = re.findall(email_pattern, text_emails)
if emails_found:
    print("Email addresses found : ", emails_found)
else:
    print("Email Addresses not found.")