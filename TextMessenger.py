#Code snippets from https://github.com/TwilioDevEd/api-snippets/blob/master/rest/messages/send-sms/send-sms.5.x.py

from twilio.rest import TwilioRestClient
import TwilioAccountDetails as myDetails

client = TwilioRestClient(account = myDetails.SID(), token = myDetails.TOKEN())

print('Welcome to the Text Messenger!')
recipient = input('Who would you like to message?\n>>> ')
message = input('What message should be sent to {}?\n>>> '.format(recipient))

client.messages.create(
    to = myDetails.number(recipient),
    from_ = myDetails.twilionumber(),
    body = message)

print('''Message Sent!
TO: {to}
MESSAGE: {message}'''.format(to = recipient, message = message))
