import requests
import asyncio
import json

from walkoff_app_sdk.app_base import AppBase

class Asd37fff3ea5fa10cdde521f21134320c26(AppBase):
    """
    Autogenerated class by Shuffler
    """
    
    __version__ = "1.0"
    app_name = "Asd37fff3ea5fa10cdde521f21134320c26"
    
    def __init__(self, redis, logger, console_logger=None):
    	self.verify = False
    	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    	super().__init__(redis, logger, console_logger)

    async def get_hello(self, apikey):
        headers={}
        url=f"https://google.com/lol"
        headers["what"] = apikey
        
        return requests.get(url, headers=headers).text
	

if __name__ == "__main__":
    asyncio.run(Asd37fff3ea5fa10cdde521f21134320c26.run(), debug=True)