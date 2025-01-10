import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format = '[%(asctime)s]: %(message)s')

files = [
    'src/__init__.py', 
    'src/helper.py',
    'prompt/__init__.py',
    'prompt/prompt.py',
    'templates',
    'static',
    '.env'
]

for f in files:
    filepath = Path(f)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating DIR: {filedir}')
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w"):
            pass
            logging.info(f"Creating filename: {filename} in {filepath}")
    else:
        logging.info(f"File: {filename} already exists at: {filepath}")