import asyncio
import aiohttp
import aiofiles

async def download_image(session, url, filename):
    print(f"Starting download: {filename}")
    async with session.get(url) as response:
        if response.status == 200:
            content = await response.read()
            async with aiofiles.open(filename, 'wb') as f:
                await f.write(content)
            print(f"Image downloaded successfully as {filename}")

async def func1(session):
    print("func1")
    await download_image(
        session,
        'https://png.pngtree.com/png-clipart/20210224/ourmid/pngtree-pink-yellow-watercolor-ink-material-png-image_2934893.jpg',
        'downloaded_image1.jpg'
    )

async def func2(session):
    print("func2")
    await download_image(
        session,
        'https://png.pngtree.com/png-clipart/20201223/ourmid/pngtree-red-watercolor-smudge-graffiti-elements-png-image_2595356.jpg',
        'downloaded_image2.jpg'
    )

async def func3(session):
    print("func3")
    await download_image(
        session,
        'https://w7.pngwing.com/pngs/114/579/png-transparent-pink-cross-stroke-ink-brush-pen-red-ink-brush-ink-leave-the-material-text.png',
        'downloaded_image3.jpg'
    )

async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            func1(session),
            func2(session),
            func3(session),
        )
    print("All downloads completed!")

if __name__ == "__main__":
    asyncio.run(main())


#what asyncio basically does is that it executes all the functions together at once, instead of one by one. 
