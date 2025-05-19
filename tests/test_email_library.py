import yagmail, sys
sys.path.insert(1, "../source")

from api import GMAIL_API_KEY

sender = input("Enter sender email address >> ")
dest = input("Enter client email address >> ")

yagmail.register(sender, GMAIL_API_KEY)

smtp = yagmail.SMTP(sender, GMAIL_API_KEY)
smtp.send(dest, "Hello world", "")
