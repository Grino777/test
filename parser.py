import json

from pydantic import ValidationError
from classes.datainfo import DataInfo

def get_incoming_text():
    with open('data.txt', 'r', encoding='utf-8') as file:
        data = file.read().replace('\n', ' ')
    return data

    # with open('data.json', 'r', encoding='utf-8') as file:
    #     data = json.load(file)
    #     print(data)
    #     return data


def main():
    try:
        # data = DataInfo.parse_file('data.txt')
        # print(data)
        data = DataInfo.parse_raw(get_incoming_text())
        with open('result.json', 'w', encoding='utf-8') as file:
            json.dump(data.dict(by_alias=True), file, indent=4, ensure_ascii=False)
    except ValidationError as e:
        print(e.errors())


if __name__ == '__main__':
    main()
