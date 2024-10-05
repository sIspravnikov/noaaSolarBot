import requests
import translators as ts

class Text:
    def __init__(self, url: str, translator: str) -> None:
        self.url = url
        self.translator = translator
    # нужно обрезать результат, в одно сообщение не влезает
    def getText(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except Exception as exception:
            print(f"{exception}")
            return("Не удалось получить дискуссию, проблема на стороне источника")
        else:
            if response.ok:
                print(response)
                try:
                    translated = ts.translate_text(query_text = response.text, translator = self.translator, from_language="en", to_language = "ru")
                except Exception as e:
                    return("Не удалось получить перевод")
                else:
                    return(str(translated))