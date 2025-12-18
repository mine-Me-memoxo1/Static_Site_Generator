import os
import shutil
from markdown_blocks import markdown_to_html_node

def src_to_dest(src=os.path.abspath('./static'), dest=os.path.abspath('./public')):
    if not os.path.exists(src):
        raise ValueError('Source path does not exist')
    elif os.path.isfile(src):
        raise ValueError('Input path is not a directory')
    
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    print(f'Copying files from {src} to {dest}')
    print(f'Copying all of {os.listdir(src)}')
    files = os.listdir(src)
    for file in files:
        ab_path = os.path.abspath(os.path.join(src, file))
        if os.path.isfile(ab_path):
            new_file_path = shutil.copy(ab_path, dest)
            print(f'{new_file_path} successfully copied')
        else:
            new_dir_path = os.path.join(dest, file)
            src_to_dest(ab_path, new_dir_path)


def extract_title(markdown):
    lines = markdown.split('\n\n')
    for line in lines:
        if line[0:2] == '# ':
            return line[2::].strip()
    raise ValueError('No h1 header in markdown file')


def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path) as file:
        markdown = file.read().strip()
        
        with open(template_path) as t_file:
            content = t_file.read().strip()
            html_code_string = markdown_to_html_node(markdown).to_html()
            
            title = extract_title(markdown)
            content = content.replace('{{ Title }}', title)
            content = content.replace('{{ Content }}', html_code_string)
            
            dest_directory = os.path.dirname(dest_path)
            os.makedirs(dest_directory, exist_ok=True)
            with open(dest_path, 'w') as d_path:
                d_path.write(content)

