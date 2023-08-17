import time
import config
import asyncio
from pyrogram import Client

app = Client("anon", api_id=config.API_ID, api_hash=config.API_HASH)

async def main():
    last_time_string = ''
    
    while True:
        local_time = time.localtime()
        new_first_name = time.strftime("%H:", local_time)
        new_last_name = time.strftime("%M", local_time)
        
        try:
            await app.update_profile(first_name=new_first_name, last_name=new_last_name)
        except Exception as e:
            print(f"Error updating profile: {e}")
        
        await asyncio.sleep(60)

app.start()
app.run(main())
