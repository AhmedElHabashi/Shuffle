import requests
import asyncio
import json
import urllib3

from walkoff_app_sdk.app_base import AppBase

class UberAPI795ed46f2dbd43d69d0c1f6b9cce14ea(AppBase):
    """
    Autogenerated class by Shuffler
    """
    
    __version__ = "1.0"
    app_name = "UberAPI795ed46f2dbd43d69d0c1f6b9cce14ea"
    
    def __init__(self, redis, logger, console_logger=None):
    	self.verify = False
    	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    	super().__init__(redis, logger, console_logger)

    async def get_price_estimates(self, start_latitude, start_longitude, end_latitude, end_longitude):
        headers={}
        url=f"https://api.uber.com/estimates/price?start_latitude={start_latitude}&start_longitude={start_longitude}&end_latitude={end_latitude}&end_longitude={end_longitude}"
        
        
        return requests.get(url, headers=headers).text
	
    async def get_time_estimates(self, start_latitude, start_longitude, customer_uuid="", product_id="", ):
        headers={}
        url=f"https://api.uber.com/estimates/time?start_latitude={start_latitude}&start_longitude={start_longitude}"
        
        
        if customer_uuid:
            url += f"&customer_uuid={customer_uuid}"
        if product_id:
            url += f"&product_id={product_id}"
        return requests.get(url, headers=headers).text
	
    async def get_user_activity(self, offset="", limit="", ):
        headers={}
        url=f"https://api.uber.com/history"
        
        
        if offset:
            url += f"&offset={offset}"
        if limit:
            url += f"&limit={limit}"
        return requests.get(url, headers=headers).text
	
    async def get_user_profile(self):
        headers={}
        url=f"https://api.uber.com/me"
        
        
        return requests.get(url, headers=headers).text
	
    async def get_product_types(self, latitude, longitude):
        headers={}
        url=f"https://api.uber.com/products?latitude={latitude}&longitude={longitude}"
        
        
        return requests.get(url, headers=headers).text
	

if __name__ == "__main__":
    asyncio.run(UberAPI795ed46f2dbd43d69d0c1f6b9cce14ea.run(), debug=True)
