import json
from classes import *

def get_incoming_text():
    with open('data.txt', 'r', encoding='utf-8') as file:
        data = file.read().replace('\n', ' ')
        # data = json.loads(data)
    return data

def main():
    # print(type(get_incoming_text()))

    try:
        data = Data.parse_raw(get_incoming_text())
        # for k, v in data.__fields__.items():
        #     print(k, v)
        print(data.json(by_alias=True))

    except ValidationError as e:
        print(e)


if __name__ == '__main__':
    main()

# ,
#     "schedule" : {
#         "id": "Never",
#     }