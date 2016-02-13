import smtplib

# Import the email modules we'll need
import sys


def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

if __name__ == '__main__':
    sendemail(from_addr='#',
              to_addr_list=[3],
              cc_addr_list=[],
              subject=sys.argv[1],
              message=sys.argv[2],
              login='#', password='#')
