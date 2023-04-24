from os import path


#ракодировать насовсем
def get_file_bytes(path_to_dir, file_name) -> bytes | None:
    file_path = path.join(path_to_dir, file_name)
    try:
        with open(file_path, "rb") as f:
            file = f.read()
            return file
    except FileNotFoundError:
        print("Не верное имя файла, \nИли не верный путь")
        return None
    except IsADirectoryError:
        print("Это дирректория")
        return None






