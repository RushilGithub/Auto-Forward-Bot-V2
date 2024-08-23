from os import environ 

class Config:
    API_ID = environ.get("API_ID", "23856851")
    API_HASH = environ.get("API_HASH", "86450d5ac4a1f0fc2421a76eab87a82c")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7093023141:AAHgzEKKgzMWWvr0dW5HnOWO0tkDQD0_EAM") 
    BOT_SESSION = environ.get("BOT_SESSION", "1BZWaqwUAUA5hYZSQPu676Sqh7jAb-bKSFTYRYKd_uSLffqqlaanbg4pZQd485aXiyr7djo4KZF00xho7D5elgUdpLeFSB-J9u4GpFuzYmDUxy9gmIUKcjVWlkBzveho3lK3hEDLVHtZYgq73CH8j-UKUDrImEPU8NeZE2b3OssafSuqF-chwrRd3ZQ_h81Vo6m0KUpur3WBy13ijwhnh3cjj9bbKBwO8CZwo9ulfDdw8-2GD17KbCHiH35ZWVW0vOFbw4H8f5y3KQloiL4yIPnJe0RsaQL9eH_EuZNez1dSlh_aotoOJiLwoquglQU-jYJM1ttLszBQ5XtWEQuyGoHgVQdODo7Y=") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7233931978').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
