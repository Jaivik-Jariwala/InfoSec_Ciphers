import logging

1

#configure logging by changing level = logging --> to error
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        logging.error("division by zero error")
    else:
        logging.info("result is :{result}")



#perform division
divide(10,2)
divide(10,0)

