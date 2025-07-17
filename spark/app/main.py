import subprocess
import logging

# logging set
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('main.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

scripts = ['extract.py', 'transform.py', 'load.py']

for script in scripts:
    logger.info(f"Running {script} ...")
    result = subprocess.run(["python", script])
    if result.returncode != 0:
        logger.error(f"{script} failed!")
        break
    else:
        logger.info(f"{script} completed successfully.")
