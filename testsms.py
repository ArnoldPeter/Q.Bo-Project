# we import the Twilio client from the dependency we just installed
from twilio.rest import Client


def SendSMS(message):
    # the following line needs your Twilio Account SID and Auth Token
    client = Client("AC3aede748210f547a02e9d406efcadcbb", "aed1fcdef064d13b76758b162796c342")

    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to  send SMS to any phone number
    client.messages.create(to="+436642375066", 
                        from_="+12029913651", 
                        body=message)

SendSMS("Help me! I have fallen! Sent by the Q.Bo Robot! ")