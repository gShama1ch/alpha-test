import json 

new_data = {
    "quality": {
                "COMP_SIZE": "Размер компании",
                "VALUE": "МСБ"
                }
            }


def update_json(json_file_path: str, new_data: dict, output_file_path=None, encoding:str='utf-8'):
    data = open(json_file_path, 'r', encoding=encoding)
    data_dict = json.load(data)
    data.close()

    data_dict = {**data_dict, **new_data}

    if output_file_path is not None:
        with open(output_file_path, 'w', encoding=encoding) as file:
            file.write(json.dumps(data_dict, ensure_ascii=False, indent=4))
            file.close()
            print(f'Complete ! File saved successfully in {output_file_path}!')
    else:
        with open(json_file_path, 'w', encoding=encoding) as file:
            file.write(json.dumps(data_dict, ensure_ascii=False, indent=4))
            file.close()
            print(f'Complete ! File updated successfully in {json_file_path}!')


if __name__ == '__main__':
    update_json(json_file_path='./data_test.json', 
                new_data=new_data, 
                output_file_path='./new_data_test.json')





