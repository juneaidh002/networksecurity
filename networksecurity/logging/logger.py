import logging
import os
from datetime import datetime
from pathlib import Path 

BASE_DIR = Path(__file__).resolve().parent.parent
date_folder = datetime.now().strftime("%Y-%m-%d")
log_file = f"{datetime.now().strftime('%H_%M_%S')}.log"

logs_dir = BASE_DIR/"logs"/date_folder
os.makedirs(logs_dir, exist_ok=True)

log_file_path = logs_dir/log_file

logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logging.info("Logger initialized")