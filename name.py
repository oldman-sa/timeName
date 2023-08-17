import time
import config
import asyncio
from pyrogram import Client

app = Client("anon", api_id=config.API_ID, api_hash=config.API_HASH)


async def main():
    last_update = 0

    while True:
        local_time = time.localtime()
        new_first_name = time.strftime("%H:", local_time)
        new_last_name = time.strftime("%M", local_time)
        
        if last_update != new_last_name:
            try:
                await app.update_profile(first_name=new_first_name, last_name=new_last_name)
                last_update = new_last_name
            except Exception as e:
                print(f"Error updating profile: {e}")

        await asyncio.sleep(1)

app.start()
app.run(main())
