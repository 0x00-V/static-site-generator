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


if __name__ == "__main__":
    copytodst("./static", "./public")
    node = TextNode("smth", TextType.BOLD)
    print(node)