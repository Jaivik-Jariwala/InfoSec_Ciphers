import logging

'''
functions included
--> debug()
--> info()
--> error()
-->critical()
'''

#configure the root logger
logging.basicConfig(level=logging.INFO)

#create logger for the specific module
logger = logging.getLogger('app')

# create file handler
file_handler = logging.FileHandler('app.log')

#console handler 
console_handler = logging.StreamHandler()

#creae formatter 
formatter = logging.Formatter('%(action)s - %(levelname)s - %(message)s')

#attach formatter to handler
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

#attach the handler to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
'if we comment this line the log wont be displayed'

#log messagesar different levels
logger.debug('this is a debug message')
logger.info('this is an info message')
logger.warning('this is a warning message')
logger.error('this is an error message')
logger.critical('this is a critical message')