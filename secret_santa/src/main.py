import polars as pl
from twilio.rest import Client
import toml

class Secret_Santa: 
    def __init__(self, account_sid : str, auth_token : str, account_number : str) -> None: 
        account_sid = account_sid

        auth_token = auth_token
        self.account_number = account_number
        self.client = Client(account_sid, auth_token)
    
    def __filter_unwanted_matches(self): 
        pass 
    def send_messages(self, filter_list = None): 
        message = self.client.messages.create(
            body="This is a test phone message",
            from_=self.account_number,
            to="+",
        )
        print(message.body)
