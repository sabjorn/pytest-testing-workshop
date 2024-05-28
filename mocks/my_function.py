from dataclasses import dataclass
import requests

@dataclass
class Palette:
    name: str
    author: str
    colors: list[str]

def function_under_test(palette_name: str) -> Palette:
    url = f"https://Lospec.com/palette-list/{palette_name}"
    
    r = requests.get(url)
    j = r.json()

    palette = Palette(**j)
    
    return palette
