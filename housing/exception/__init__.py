import os
import sys

class HousingException(Exception): #passing over the main python exception module.
    
    def __init__(self, error_message:Exception, error_detail:sys):
        super().__init__(error_message) #passing the error_msg to the Excptn class = Exception(error_msg)
        self.error_message=HousingException.get_detailed_error_message(error_message=error_message,
                                                                       error_detail=error_detail
                                                                        )


    @staticmethod # so that we don call the function by name, instead we jxt use the class name to access.
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
        """
        error_message: Exception object
        error_detail: object of sys module
        """
        _,_ ,exec_tb = error_detail.exc_info() # -> return(name,type,traceback), so we just need the _,_,traceback.
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        
        error_message = f"Error occured in script: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"
        return error_message

    def __str__(self):
        return self.error_message


    def __repr__(self) -> str:
        return HousingException.__name__.str()
