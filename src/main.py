from helpers import copy_to_directory, generate_page
import shutil
import os


def main():
    if os.path.exists("public"):
        print("Cleaning public directory")
        shutil.rmtree("public")

    copy_to_directory("static", "public")

    generate_page("content/index.md", "template.html", "public/index.html")


main()
