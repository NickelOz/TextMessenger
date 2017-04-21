#Code snippets from https://github.com/TwilioDevEd/api-snippets/blob/master/rest/messages/send-sms/send-sms.5.x.py

#load twilio and python modules
from twilio.rest import TwilioRestClient
import TwilioAccountDetails as myDetails
import time
import textwrap

client = TwilioRestClient(account = myDetails.SID(), token = myDetails.TOKEN())

#get message
print('Welcome to the Text Messenger!')
recipient = input('Who would you like to message?\n>>> ')
message = input('What message should be sent to {}?\n>>> '.format(recipient))

#send message through twilio
client.messages.create(
    to = myDetails.number(recipient),
    from_ = myDetails.twilionumber(),
    body = message)

#display message to user
print('''Message Sent!
TO: {to}
MESSAGE: {message}'''.format(to = recipient, message = message))

#log message details
with open('MessageRecord.txt', 'a') as record:
    record.write('=' * 48 +
                 '\nTIMESTAMP:'.ljust(13) + #newline counts as a character
                 '{}\n'.format(time.strftime('%A, %d of %B %Y, %I:%M%p')) +
                 'TO:'.ljust(12) +
                 '{}\n'.format(recipient) +
                 'FROM:'.ljust(12) +
                 '{}\n'.format(myDetails.me()) +
                 'MESSAGE:'.ljust(12) +
                 '{}\n'.format(message))
