import logging 
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',

    handlers=[
        logging.FileHandler('app.py'),
        # logging.StreamHandler()
    ]  

    )

logger = logging.getLogger('Arthimatic')

def add(a,b):
    result = a+b
    logger.debug(f"adding{a} + {b} = {result}")
    return result

add(3,4)
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")

