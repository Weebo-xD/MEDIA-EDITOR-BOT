import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5092511287:AAFUfE-_ZCBezMUhrzSTiinMW52XRppKYr8")

    APP_ID = int(os.environ.get("APP_ID", 1995654))

    API_HASH = os.environ.get("API_HASH", "91aa713a74d1bccb50cd1c03758316bf")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "860540443").split())
  
    
