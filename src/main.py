from textnode import *
import shutil, os, sys

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


def generate_page(src, template, dst, basepath):
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
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')


    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w") as dst_file:
        dst_file.write(html)

def generate_pages_recursive(src, template, dst, basepath):
    if not os.path.exists(src):
        raise Exception("Location doesn't exist!")
    os.makedirs(dst, exist_ok=True)
    items = os.listdir(src)
    for item in items:
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isfile(src_path):
            if src_path.endswith(".md"):
                dst_path = dst_path.replace(".md", ".html")
                generate_page(src_path, template, dst_path, basepath)
        else:
            generate_pages_recursive(src_path, template, dst_path, basepath)

#




if __name__ == "__main__":
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copytodst("./static", "./docs")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)