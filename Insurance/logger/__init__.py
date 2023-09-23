from datetime import datetime
import sys,os
import logging

LOG_DIR = "Insurance_log"

CURRENT_TIMESTAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

LOG_FIlE_NAME = f"log_{CURRENT_TIMESTAMP}.log"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FIlE_PATH = os.path.join(LOG_DIR, LOG_FIlE_NAME)

logging.basicConfig(filename=LOG_FIlE_PATH,
filemode = "w",
format = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
#level=logging.INFO,
level=logging.DEBUG,
)
