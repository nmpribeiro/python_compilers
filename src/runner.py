from src.utils import read_file


def main():
    # repl()
    import sys
    from os.path import exists

    if len(sys.argv) < 2:
        print("file not given.")
        sys.exit(0)
    file_name = sys.argv[1]

    if not exists(file_name):
        print(f"{file_name} not found")
        sys.exit(0)

    read_file(file_name)
