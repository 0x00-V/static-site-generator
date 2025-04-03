from textnode import *
import shutil, os

def copytodst(static, public):
    if os.path.exists(public):
        shutil.rmtree(public)
    os.mkdir(public)
    
    items = os.listdir(static)
    for item in items:
        static_path = os.path.join(static, item)
        public_path = os.path.join(public, item)
        if os.path.isfile(static_path):
            print(f"FILE: {item} {static} -> {public}")
            shutil.copy(static_path, public_path)
        else:
            print(f"Directory Created ({item}): {public}")
            os.mkdir(public_path)
            copytodst(static_path, public_path)

def extract_title(md):
    md_lines = md.splitlines()
    for line in md_lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No h1 header found.")


def generate_page(src, template, dst):
    print(f"Generating page: {src} -> {dst} | Using: {template}")

    with open(src, "r") as md_file:
        markdown_content = md_file.read()
    with open(template, "r") as template_file:
        template_content = template_file.read()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    title = extract_title(markdown_content)

    html = template_content.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", html_content)


    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w") as dst_file:
        dst_file.write(html)
    

if __name__ == "__main__":
    copytodst("./static", "./public")
    generate_page("./content/index.md", "./template.html", "./public/index.html")