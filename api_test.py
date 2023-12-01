import requests

search = {id:76561198337392994, name:"Lubbsies", character:"Jack-O'"}


response = requests.post("https://ggst-game.guiltygear.com/api/catalog/get_replay", id=id, name=name, character=character)