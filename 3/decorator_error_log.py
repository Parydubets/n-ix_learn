import logging

class CustomException(Exception):
    pass

def log(func):
    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        fh = logging.FileHandler("%s.log" % name)
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info("function call: %s" % name)
        try:
            logger.info("The input: %s" % args[0])
            result = func(*args, **kwargs)
            logger.info("Result: %s" % result)
        except Exception as e:
            logger.error(e)
            raise CustomException("%s" % e)
        return func
    return wrap_log


@log
def test_func(n):
    return (n/0)

if __name__ == "__main__":
    value = test_func(25)