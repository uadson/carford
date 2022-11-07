import random
import os
from pathlib import Path, PurePosixPath, PureWindowsPath
from string import ascii_letters, digits


# Config data
chars = "!?@#$%^&*()" + ascii_letters + digits
size = 57
secret_key = "".join(random.sample(chars, size))

# Paths
BASE = Path(__file__).resolve().parent.parent


CONFIGS = f"""# Development Config
SECRET_KEY = '{secret_key}'
DEBUG = 'True'
ALLOWED_HOSTS = '127.0.0.1'
"""


if os.name == 'nt':
# To Windows
    BACKEND = PureWindowsPath(BASE).joinpath('carford')
    SETTINGS = PureWindowsPath(BACKEND).joinpath('settings')

    with open(f'{SETTINGS}\.env', 'w') as settings_file:
        settings_file.write(CONFIGS)
else:
    # To Linux
    BACKEND = PurePosixPath(BASE).joinpath('carford')
    SETTINGS = PurePosixPath(BACKEND).joinpath('settings')
    
    with open(f'{SETTINGS}/.env', 'w') as settings_file:
        settings_file.write(CONFIGS)


if __name__ == '__main__':
    ...