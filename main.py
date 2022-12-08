from pprint import pprint

import requests

# Задание 1
req_all = requests.get('https://akabab.github.io/superhero-api/api/all.json')
all_info = req_all.json()


def heroname(name):
    for hero in all_info:
        if name == hero.get("name"):
            return hero.get('id')


def herostatintelligence(name):
    id_hero = heroname(name)
    for hero in all_info:
        if id_hero == hero.get('id'):
            url_hero = f"https://akabab.github.io/superhero-api/api/powerstats/{id_hero}.json"
            url_hero_get = requests.get(url_hero)
            readable_hero_stat = url_hero_get.json()
            intel = readable_hero_stat.get('intelligence')
            return intel


def most_clever(list_):
    heroes_int = {

    }
    for hero in list_:
        hero_int = herostatintelligence(hero)
        heroes_int[hero] = hero_int
    max_val = max(heroes_int.values())
    final_dict = {k: v for k, v in heroes_int.items() if v == max_val}
    names = final_dict.keys()
    for name in names:
        return name


hero_list = ["Hulk", 'Captain America', 'Thanos']
print(most_clever(hero_list))

# Задача 2
# 1
# 1
# 1


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    files_url = "https://cloud-api.yandex.net/v1/disk/resources/files"
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

    @property
    def headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    def get_upload_link(self, file_path: str) -> dict:
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(self.upload_url, params=params, headers=self.headers)
        jsonify = response.json()
        pprint(jsonify)
        return jsonify


    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self.get_upload_link(file_path).get("href")
        if not href:
            return

        with open(file_path, 'rb') as file:
            response = requests.put(href, data=file)
            if response.status_code == 201:
                print("файл загружен")
                return True
            print("файл не загружен потому что", response.status_code)
            return False


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "https://github.com/AlexaLeb/netologyHomeWork/blob/ed4a32675c45cf0177dc23825897f9209487ebef/filetxt.txt"
    token = "тут должен быть токен"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
