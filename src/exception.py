# This file is for halding the exception.


# sys module provides various functions and variables that are used to manipulate different parts of the Python runtime environment.

import sys
from src.logger import logging
import logging


def error_message_detail(error, error_detail:sys): # Whenever error gets raised, i want to pass my own message. custom exception handline.
    _,_,exc_tb=error_detail.exc_info() # provides information where, wihch line the error has occured and store in exc_tb variable.
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))    

    return error_message



class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)


    def __str__(self):
        return self.error_message
    


# Checking 
# if __name__ == '__main__':
#     try: 
#         a = 1/0

#     except Exception as e:
#         logging.info('Divide by zero error.')
#         raise CustomException(e, sys)