import logging
import os


class Crawler:
    def __init__(self,
                 root_path: str,
                 venv_abspath: str):
        self._log = logging.getLogger('gsts.crawler')

        self._root_path = os.path.abspath(root_path)

        if os.path.exists(venv_abspath):
            self._venv_abspath = venv_abspath
        else:
            self._venv_abspath = None

    def scan_project(self):
        return self._scan_dir(self._root_path, self._venv_abspath)

    def _scan_dir(self,
                  dir_path: str,
                  venv_abspath: str):
        python_files = []

        with os.scandir(dir_path) as dir:
            for entry in dir:
                abspath = os.path.abspath(entry.path)

                if entry.is_file() and entry.name.endswith('.py'):
                    self._log.debug('Add .py: ' + abspath)
                    python_files.append(abspath)

                elif entry.is_dir() and abspath != venv_abspath:
                    self._log.debug('Scanning dir: ' + abspath)
                    python_files.extend(self._scan_dir(entry.path, venv_abspath))

        return python_files
