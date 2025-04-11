from helpers import copy_to_directory, generate_pages_recursive
import shutil
import os
import sys


def main():
    base_path = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]

    if os.path.exists("docs"):
        print("Cleaning docs directory")
        shutil.rmtree("docs")

    copy_to_directory("static", "docs")

    generate_pages_recursive("content", "template.html", "docs", base_path)


main()
