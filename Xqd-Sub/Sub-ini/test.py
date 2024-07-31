import os

def convert_list_to_yaml(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    yaml_content = 'rules:\n'
    for line in lines:
        yaml_content += f'  - {line.strip()}\n'

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(yaml_content)

def convert_all_lists_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.list'):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename.replace('.list', '.yaml'))
            convert_list_to_yaml(input_file, output_file)
            print(f'Converted {input_file} to {output_file}')

# 使用示例
input_folder = r'D:\Desktop\Xqd-Sub-main\Xqd-Sub'
output_folder = os.path.join(input_folder, 'converted_yaml_files')
convert_all_lists_in_folder(input_folder, output_folder)
