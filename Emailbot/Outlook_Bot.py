from config import *
import time
import pyzmail
import imapclient
import smtplib
import email.message

subject = "Python"

def imap_init():
    """
    Initialize IMAP connection
    """
    print("Initializing IMAP... ", end='')
    global i
    i = imapclient.IMAPClient(imapserver)
    c = i.login(radr, pwd)
    i.select_folder("INBOX", readonly=True)
    print("Done. ")

def smtp_init():
    """
    Initialize SMTP connection
    """
    print("Initializing SMTP...")
    global s
    s = smtplib.SMTP(smtpserver, smtpserverport)
    c = s.starttls()[0]  # The returned status code
    if c is not 220:
        raise Exception('Starting tls failed: ' + str(c))
    c = s.login(radr, pwd)[0]
    if c is not 235:
        raise Exception('SMTP login failed: ' + str(c))
    print("Done. ")

def get_unread():
    """
    Fetch unread emails
    """
    global i
    uids = i.search(['UNSEEN'])
    if not uids:
        return None
    else:
        print("Found %s unreads" % len(uids))
        return i.fetch(uids, ['BODY[]', 'FLAGS'])

def analyze_msg(raws, a):
    """
    Analyze message.  Determine if sender and command are valid.
    Return values:
    None: Sender is invalid or no text part
    False: Invalid command
    Otherwise:
    Array: message split by lines
    :type raws: dict
    """
    print("Analyzing message with uid " + str(a))
    msg = pyzmail.PyzMessage.factory(raws[a][b'BODY[]'])
    frm = msg.get_addresses('from')
    if frm[0][1] != sadr:
        print("Unread is from %s <%s> skipping" % (frm[0][0],
                                                   frm[0][1]))
        return None
    global subject
    if not subject.startswith("Re"):
        subject = "Re: " + msg.get_subject()
    print("subject is", subject)
    if msg.text_part is None:
        print("No text part, cannot parse")
        return None
    text = msg.text_part.get_payload().decode(msg.text_part.charset)
    cmds = text.replace('\r', '').split('\n')  # Remove any \r and split on \n
    if cmds[0] not in commands:
        print("Command %s is not in commands" % cmds[0])
        return False
    else:
        return cmds

def mail(text):
    """
    Print an email to console, then send it
    """
    print("This email will be sent: ")
    print(text)
    msg = email.message.EmailMessage()
    global subject
    msg["from"] = radr
    msg["to"] = sadr
    msg["Subject"] = subject
    msg.set_content(text)
    res = s.send_message(msg)
    print("Sent, res is", res)

imap_init()
smtp_init()

while True:  # Main loop
    try:
        print()  # Blank line for clarity
        msgs = get_unread()
        while msgs is None:
            time.sleep(check_freq)
            msgs = get_unread()
        for a in msgs.keys():
            if type(a) is not int:
                continue
            cmds = analyze_msg(msgs, a)
            if cmds is None:
                continue
            elif cmds is False:  # Invalid Command
                t = "The command is invalid. The commands are: \n"
                for l in commands.keys():
                    t = t + str(l) + "\n"
                mail(t)
                continue
            else:
                print("Command received: \n%s" % cmds)
                r = commands[cmds[0]](cmds)
            mail(str(r))
            print("Command successfully completed! ")
    except KeyboardInterrupt:
        i.logout()
        s.quit()
        break
    except OSError:
        imap_init()
        continue
    except smtplib.SMTPServerDisconnected:
        smtp_init()
        continue
    finally:
        i.logout()
        s.quit()