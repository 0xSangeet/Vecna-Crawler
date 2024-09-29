from join import client

async def download():
    with open('links.txt', 'r') as f:
        to_crawl = [x.strip() for x in f.readlines()]
    for link in to_crawl:
        messages = client.iter_messages(link, 2)
        async for message in messages:
            try:
                if message.media.document.mime_type == 'text/plain':
                    print(f'Downloading file: {message.media.document.attributes[0].file_name}')
                    await client.download_media(message)
            except Exception as e:
                print('Message skipped')

async def crawl_main():
    await download()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(crawl_main())