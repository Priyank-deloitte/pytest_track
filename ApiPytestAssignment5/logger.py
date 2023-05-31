import inspect
import logging


class log_class:
    @staticmethod
    def custom_logger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(
            loggerName)  # it will tell that right now this particular test file is being run and the logs are printed in regarding to that test file
        filename = logging.FileHandler(
            'LogReport\\logfile.log')  # fileHandler method gives info. about the logging file where all the logs will be printed
        formatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p")  # here the format is decided like in what format the log message is printed
        filename.setFormatter(
            formatter)  # here the format is appended to filehandler to pass the format info. to log file

        logger.addHandler(filename)

        logger.setLevel(
            logging.INFO)  # it will now print all the messages from and below the info level and skip the debug messages

        return logger
