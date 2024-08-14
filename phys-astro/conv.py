import os
import re

def convert_math_delimiters(content):
    # 先處理 displaystyle math
    # 使用正則表達式處理不被反斜線轉義的 $$...$$
    content = re.sub(r'(?<!\\)\$\$(.*?)\$\$', r'\[\1\]', content, flags=re.DOTALL)
    
    # 然後處理 inline math
    # 使用正則表達式處理不被反斜線轉義的 $...$
    content = re.sub(r'(?<!\\)\$(.*?)\$', r'\(\1\)', content)


    return content

def process_markdown_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            new_content = convert_math_delimiters(content)

            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f'Processed {filename}')

# 使用當前目錄
process_markdown_files('.')
