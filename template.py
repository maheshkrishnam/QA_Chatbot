import os
import logging
from pathlib import Path

list_files = [
    "QAWithData/__init__.py",
    "QAWithData/data_ingestion.py",
    "QAWithData/embeddings.py",
    "QAWithData/model_api.py",
    "Experimentas/experiments.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "exception.py",
    "setup.py"
]

for filepath in list_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    print(f'Filedir : {filedir} | Filename : {filename}')
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created Directory: {filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass