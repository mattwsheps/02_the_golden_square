import os
from twilio.rest import Client

class TextSender:
    def __init__(self):
        """
        Attributes:
            account_sid: a string representing the account sid
            auth_token: a string representing the authorisation token
            twilio_phone_no: a string representing the twilio phone number
                            which will send the message
        """

        self.account_sid = 'YOUR_ACCOUNT_SID'
        self.auth_token = 'YOUR_AUTH_TOKEN'
        self.twilio_phone_no = 'YOUR_PHONE_NUMBER'

    def send_text(self, phone_no, confirmation_message):
        """
        Parameters:
            phone_no: a string representing a phone number
            message: a string representing the message to be sent
        Side effects:
            Sends the message as an SMS to the phone number using twilio
        """
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
                .create(
                    body=confirmation_message,
                    from_=self.twilio_phone_no,
                    to=phone_no
                )