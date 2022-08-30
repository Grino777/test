from pydantic import BaseModel
import json

# def incoming_text(data=None):



def main():

    with open('data.txt', 'r', encoding='utf-8') as file:
        data = file.read().replace('\n', '')
        data = json.loads(data)

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    main()