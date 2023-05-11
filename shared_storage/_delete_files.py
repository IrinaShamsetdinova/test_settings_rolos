from pathlib import Path
from shutil import rmtree


for path in Path('/home/coder/project/.rolos_storages/shared').glob('*'):
    if path.is_dir():
        rmtree(path)
    else:
        path.unlink()