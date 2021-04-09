radr = input("Adresses to log in to")  # address to check and send from
imapserver = input("IMAP server domain: ")  # imap server for account
smtpserver = input("SMTP server domain: ")  # smtp server for account
smtpserverport = input("SMTP Server port [587]: ")  # smtp server port for starttls
if not smtpserverport or smtpserverport == "":
    smtpserverport = 587
pwd =  getpass.getpass("Account password: ") # password for account encoded with base64.b64encode
sadr = input("Trusted addresses to receive from: ")  # address to receive commands from
check_freq = 5