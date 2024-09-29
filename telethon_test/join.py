from telethon.tl.functions.channels import JoinChannelRequest
from telethon import TelegramClient
import os

api_id = 12345678
api_hash = 'kjygiugyguyguyfkyufuf'
client = TelegramClient('anon', api_id, api_hash)
limit = 1

async def joinChannels():
    with open('links.txt', 'r') as f:
        try:
            for i in range(limit):
                link = f.readline()
                await client(JoinChannelRequest(link.replace('\n', '')))
                print(f"Successfully joined {link}")
        except:
            print(f"Failed to join {link}")


async def join_main():
    await joinChannels()
    
if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(join_main())
