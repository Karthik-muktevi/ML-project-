### Testing logger and exception

from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os,sys


def test_log_exc():
    try:
        logging.info('start')
        x = 3/0
        print(x)
        logging.info('end')
    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e,sys)    
    
if __name__ == "__main__":
    try:
        test_log_exc()
    except Exception as e:
        print(e)