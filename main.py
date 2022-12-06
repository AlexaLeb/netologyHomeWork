from pprint import pprint

import requests
#
# res = requests.get('http://google.com')
# print(res)
# print(res.text)

class YandexDisk:
    files_url = "https://cloud-api.yandex.net/v1/disk/resources/files"
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

    def __init__(self, token: str):
        self.token = token

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

    def upload(self, file_path):
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

def get_token():
    with open("/Users/yulialebedeva/Desktop/Work/netologyHomeWork/tokeen", 'r') as file:
        return file.readline()



ya_client = YandexDisk(get_token())
ya_client.upload('списокрецептов.txt')