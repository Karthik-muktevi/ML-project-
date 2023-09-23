import os,sys

class InsuranceException(Exception):
    def __init__(self,error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message = InsuranceException.error_message_detail(error_message=error_message, error_detail=error_detail)

    @staticmethod
    def error_message_detail(error_message:Exception,error_detail:sys)->str:
        
        _,_,exec_tb = error_detail.exc_info()
        try_block_lineno = exec_tb.tb_lineno
        exception_block_lineno = exec_tb.tb_frame.f_lineno
        filename = exec_tb.tb_frame.f_code.co_filename
        error_message = f"""
        Error occured in execution of :[{filename}] at try block number: [{try_block_lineno}]
        and execption block number : [{exception_block_lineno}]
        error_message : [{error_message}]
"""
        return error_message
    
    def __str__(self):
        """
        Formating how a object should be visible if used in print statement.
        """
        return self.error_message


    def __repr__(self):
        """
        Formating object of AppException
        """
        return InsuranceException.__name__.__str__()