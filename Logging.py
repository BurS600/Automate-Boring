import logging

logging.basicConfig(filename="mylog.txt",level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
# first parameter creates a log file in cwd
# second parameter (need to research if it can have different level names for you to create)
# third parameter adds useful info to the log message like timestamp


# logging.disable(logging.CRITICAL)
# disables all log messages at CRITICAL level and below


logging.debug('Start of Program')

def factorial(n):
    logging.debug('Start of factorial of (%s):' % (n) )
    # can write log messages at various levels in following ascending order: debug, info, warning, error, critical
    total = 1
    for i in range(1 , n+1):
        total *= i
        logging.debug('i is %s, total is %s ' % (i, total) )

    logging.debug('Return value post completing of function is %s' % (total))
    return total

print(factorial(5))
print(factorial(3))

logging.debug('End of Program')


