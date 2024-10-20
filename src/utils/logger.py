import logging
import os, errno

def mkdir_p(path):
    try:
        os.makedirs(path, exist_ok=True)  # Python>3.2
    except TypeError:
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise

class Logger:
    def __init__(self, file_name: str = "bot.log", folder: str = "logs"):
        mkdir_p(str(folder))
        self.log_path = f'{folder}/{file_name}'

        logging.root.handlers = []
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        self.__config()
    
    def __config(self):
        self.formatter = logging.Formatter('%(levelname)s | %(asctime)s - %(message)s', datefmt='%Y-%m-%d (%a) %H:%M:%S')

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.formatter)

        file_handler = logging.FileHandler(self.log_path)
        file_handler.setFormatter(self.formatter)

        self.logger.handlers = []

        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)

    def __debug(self, message: str):
        """Log a debug message
        """
        self.logger.debug(message)

    def __info(self, message: str):
        """Log an info message
        """
        self.logger.info(message)
        print(f'{message}')
    
    def __warning(self, message: str):
        """Log a warning message
        """
        self.logger.warning(message)

    def __error(self, message: str):
        """Log an error message
        """
        self.logger.error(message)

    def __critical(self, message: str):
        """Log a critical message
        """
        self.logger.critical(message)

    def __checkLogSize(self):
        """Check the size of the log file and remove it if it exceeds 100MB. Create a new log file after.
        """
        if os.path.getsize(self.log_path) > 100000000: # 100MB
            os.remove(self.log_path)
            self.__info("Log file removed due to size limit")
            # Reconfiguring the logger
            self.__config()

    def makeLog(self, message: str, level: str):
        """Make a log message

        Args:
            message (str): Message to log
            level (str): Log level

        Raises:
            ValueError: Invalid log level
        """
        self.__checkLogSize()

        match level.upper():
            case "DEBUG":
                self.__debug(message)
            case "INFO":
                self.__info(message)
            case "WARNING":
                self.__warning(message)
            case "ERROR":
                self.__error(message)
            case "CRITICAL":
                self.__critical(message)
            case _:
                raise ValueError("Invalid log level")