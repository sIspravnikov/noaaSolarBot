import os
import shutil
import requests
from bs4 import BeautifulSoup

class NOAA:

    def __init__(self, url: str, extension: str, paths: dict) -> None:
        self.url = url
        self.extension = extension
        self.paths = {}
        for key,value in paths.items():
            self.paths[key] = (os.path.join(os.getcwd(), value))
        self._prepareFS()

    def _prepareFS(self) -> None:
        for path in self.paths.values():
            if os.path.exists(path):
                shutil.rmtree(path)
            if not os.path.exists(path):
                os.mkdir(path)

    def _downloadImage(self, source_url, path) -> None:
        try:
            response = requests.get(source_url, stream=True)
            response.raise_for_status()
        except Exception as exception:
            print(f"{exception}")
        else:
            with open(path, 'wb') as f:
                for chunk in response:
                    f.write(chunk)

    def _links2Files(self, links: list):
        for counter, url in enumerate(links):
            print(counter, url)
            self._downloadImage(url, f"{self.paths['frames']}/{counter}.{self.extension}")

    def getFiles(self) -> None:
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except Exception as exception:
            print(f"{exception}")
        else:
            if response.ok:
                soup = BeautifulSoup(response.text, 'html.parser')
                urls = [self.url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(self.extension)]
                self._links2Files(urls)
    
