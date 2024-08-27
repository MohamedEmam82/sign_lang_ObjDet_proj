import logging 
import os
from datetime import datetime

# from_root -> helps with declaring absolute paths relative to your project root
# from_here ->  comes in handy when you want to declare a path relative to the current file
from from_root import from_root

# define log file name and ext
LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y %H_%M_%S')}.log"
log_path = os.path.join(from_root(), 'log', LOG_FILE)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)
