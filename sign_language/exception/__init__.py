import sys



def error_message_detail(error, error_detail: sys):

    # tb -> python "traceback" for an exception error
    # .exc_info() -> exception information, returns the tuple (type(e), e, e.__traceback__)
    '''
    type of the exception , 
    the exception itself, 
    and a traceback object which typically encapsulates the call stack at the point where the exception last occurred.
    '''
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured python script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))

    return error_message


class SignException(Exception):

    def __init__(self, error_message, error_detail):
        # error_message -> in string format
        '''
        The super() function in Python is used to refer to the parent class. 
        When used in conjunction with the __init__() method, it allows the child class to invoke the constructor of its parent class. 
        This is especially useful when you want to add functionality to the child class’s constructor without completely overriding the parent class’s constructor.

        Combining super() with __init__() can be particularly useful when you want to extend
        the behavior of the parent class’s constructor while maintaining its functionality.
        '''
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
