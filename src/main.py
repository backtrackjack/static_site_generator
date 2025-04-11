from helpers import copy_to_directory, generate_pages_recursive
import shutil
import os


def main():
    if os.path.exists("public"):
        print("Cleaning public directory")
        shutil.rmtree("public")

    copy_to_directory("static", "public")

    generate_pages_recursive("content", "template.html", "public")


main()
