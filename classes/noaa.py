import os
import aiohttp
import aiofiles
import asyncio
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup

class NOAA:

    def __init__(self, source: str, url: str, extension: str, paths: dict) -> None:
        self.url = url
        self.extension = extension
        self.paths = {}
        for key,value in paths.items():
            self.paths[key] = (os.path.join(os.getcwd(), 'data', source, value))
        self._prepareFS()

    def _prepareFS(self) -> None:
        for path in self.paths.values():
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)

    # синхронный метод, лочит бота на время исполнения, не используем
    # def _links2Files(self, links: list) -> None:
    #     for url in tqdm(links, desc="downloading images"):
    #         try:
    #             response = requests.get(url, stream=True)
    #             response.raise_for_status()
    #         except Exception as exception:
    #             print(f"{exception}")
    #         else:
    #             with open(f"{self.paths['frames']}/{url.split('/')[-1]}", 'wb') as f:
    #                 for chunk in response:
    #                     f.write(chunk)
    # асинхронный метод
    async def _fetch(self, url, session):
        if not os.path.exists(f"{os.path.join(self.paths['frames'], url.split('/')[-1])}"):
            async with session.get(url) as response:
                if response.status == 200:
                    print(f"new file {os.path.join(self.paths['frames'], url.split('/')[-1])}")
                    file = await aiofiles.open(f"{os.path.join(self.paths['frames'], url.split('/')[-1])}", mode='wb')
                    try: 
                        await file.write(await response.read())
                        await file.close()
                        return await response.read()
                    except Exception as exception:
                        print(exception)
    # асинхронный метод
    async def _fetch_pages_parallel(self, urls: list):
        slash = '\\'
        async with aiohttp.ClientSession() as session:
            results = []
            for url in tqdm(urls, desc = f"updating {self.paths['frames'].split(slash)[-2]} files"):
                results.append(self._fetch(url, session))
            await asyncio.gather(*results)


    async def getFiles(self) -> None:
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except Exception as exception:
            print(f"{exception}")
        else:
            if response.ok:
                soup = BeautifulSoup(response.text, 'html.parser')
                urls = [self.url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(self.extension)]
                await self._fetch_pages_parallel(urls)
