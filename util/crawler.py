import os


def scan_dir(dir_path: str,
             venv_abspath: str):
    python_files = []

    with os.scandir(dir_path) as dir:
        for entry in dir:
            abspath = os.path.abspath(entry.path)

            if entry.is_file() and entry.name.endswith('.py'):
                print('add', abspath)
                python_files.append(abspath)

            elif entry.is_dir() and abspath != venv_abspath:
                python_files.extend(scan_dir(entry.path, venv_abspath))

    return python_files
