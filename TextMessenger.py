#Code snippets from https://github.com/TwilioDevEd/api-snippets/blob/master/rest/messages/send-sms/send-sms.5.x.py

from twilio.rest import TwilioRestClient
import TwilioAccountDetails as myDetails

client = TwilioRestClient(account = myDetails.SID(), token = myDetails.TOKEN())

client.messages.create(
    to = myDetails.number(),
    from_ = myDetails.twilionumber(),
    body = 'Message Success!')
