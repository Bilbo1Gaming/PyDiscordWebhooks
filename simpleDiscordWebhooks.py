"""
A simple python interface with discord webhooks.

Create a new webhookController Instance with the url and username of the webhook and use .success, .log or .error to send themed messages for that username.

A Discord webhook links to a channel and not a username therefore can be used many times per username.

By: Bilbo1Gaming
"""

import requests, datetime

class webhookController:
    """
    Create a simple interface with a discord webhook.

    """
    def __init__(self,url:str,username:str):
        """
        :param str url: The Webhook URL to send to
        :param str username: The Username of the "bot" that sends the message
        """
        
        self.url = url
        self.username = username
    
    def _sendEmbed(self, title:str, color:int, name:str, value:str):
        requests.post(self.url,json={
            "username": self.username,
            "embeds": [{
                "title": title,
                "color": color,
                "timestamp": str(datetime.datetime.now()),
                "fields": [{
                    "name": name,
                    "value": value
                }]}]})

    def success(self, title:str="", description:str=""):
        """
        Send a green success message

        :param str title: The header for the success message
        :param str description: Any other information for the sucess message
        """
        self._sendEmbed("Success", 45827, title, description)

    def error(self, title:str="", description:str=""):
        """
        Send a red error message

        :param str title: The header for the error message
        :param str description: Any other information for the error message
        """
        self._sendEmbed("Error", 11730944, title, description)
    
    def log(self, title:str="", description:str=""):
        """
        Send a blue log message

        :param str title: The header for the log message
        :param str description: Any other information for the log message
        """
        self._sendEmbed("Log", 5555, title, description)