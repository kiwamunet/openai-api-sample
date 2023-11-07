
import json
import csv
from typing import List

# ==============================================
# configからAPIキーを読み込む
# ==============================================
def load_api_key(key: str) -> dict:
    json_path = "configs/api_keys.json"  # 外から渡せるようにしてもいいかも
    try:
        keyfile = json.load(open(json_path))
        if key in keyfile:
            return keyfile[key]
        else:
            print("Looks like the keys aren't configured yet, or you entered the wrong strategy!")
        raise Exception("API KeyFile Missing!")
    except FileNotFoundError:
        print("File Not Found!")
        raise Exception("API KeyFile Missing!")






# ==============================================
# configからAPIキーを読み込む
# ==============================================
def get_csv_head(file_path: str) -> str:
    """
    指定されたCSVファイルを文字列として返す関数。

    Args:
        file_path (str): CSVファイルのパス。

    Returns:
        str: CSVファイルをカンマ区切りで連結した文字列。
    """
    text = ''

    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            text += ','.join(row) + '\n'
    return text
