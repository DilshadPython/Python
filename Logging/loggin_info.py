import logging

# print(dir(logging))

'''
['BASIC_FORMAT', 'BufferingFormatter', 'CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'FileHandler', 
'Filter', 'Filterer', 'Formatter', 'Handler', 'INFO', 'LogRecord', 'Logger', 'LoggerAdapter', 
'Manager', 'NOTSET', 'NullHandler', 'PercentStyle', 'PlaceHolder', 'RootLogger', 'StrFormatStyle', 
'StreamHandler', 'StringTemplateStyle', 'Template', 'WARN', 'WARNING', '_STYLES', '_StderrHandler', 
'__all__', '__author__', '__builtins__', '__cached__', '__date__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__path__', '__spec__', '__status__', '__version__', '_acquireLock', 
'_addHandlerRef', '_checkLevel', '_defaultFormatter', '_defaultLastResort', '_handlerList', 
'_handlers', '_levelToName', '_lock', '_logRecordFactory', '_loggerClass', '_nameToLevel', 
'_releaseLock', '_removeHandlerRef', '_showwarning', '_srcfile', '_startTime', '_warnings_showwarning', 
'addLevelName', 'atexit', 'basicConfig', 'captureWarnings', 'collections', 'critical', 'currentframe', 
'debug', 'disable', 'error', 'exception', 'fatal', 'getLevelName', 'getLogRecordFactory', 'getLogger', 
'getLoggerClass', 'info', 'io', 'lastResort', 'log', 'logMultiprocessing', 'logProcesses', 
'logThreads', 'makeLogRecord', 'os', 'raiseExceptions', 'root', 'setLogRecordFactory', 
'setLoggerClass', 'shutdown', 'sys', 'threading', 'time', 'traceback', 'warn', 'warning', 
'warnings', 'weakref']
'''

'''
Level:		Nummeric:
NOTSET 		0
DEBUG 		10
INFO 		20
WARNING 	30
ERROR 		40
CRITICAL 	50
'''

# create and configure logger
logging.basicConfig(filename='createfile.log')
logger = logging.getLogger()

''' test the logger here, we run python logging_info.py the file will be created in current path
but it will be empty file
'''
logger.info('First message')

print(logger.level)		# result it will be 30

