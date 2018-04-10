from datetime import datetime
from colorama import init, Fore
from filelock import Timeout, FileLock

def get_date_logging():
    return str(datetime.now())[11:][:-3]

# file lock is necessary to preent errors in mutlithreaded applications

class Logger: 
    def __init__(self, filename = None): 
        init(autoreset=True)
        self.lock = FileLock("log.lock")
        #if no  filename is included as a string, it assumes you don't want to create a log file
        if filename == None:
            self.logToTxt = False
        else:
            self.logToTxt = True
            self.filename = filename

    def write2file(self,text):
        with self.lock:
            with open(self.filename,'a') as file:
                file.write(text)


    def success(self, message):
        print(Fore.GREEN + "["+ get_date_logging()+"] " + message)
        if (self.logToTxt):
            self.write2file("["+ get_date_logging()+"] " + "SUCCESS: " + message + '\n')

    def warn(self, message):
        print(Fore.YELLOW + "["+ get_date_logging()+"] " + message)
        if (self.logToTxt):
            self.write2file("["+ get_date_logging()+"] " + "WARNING: " + message + '\n')

    def log(self, message):
        print(Fore.BLUE + "["+ get_date_logging()+"] " + message)
        if (self.logToTxt):
            self.write2file("["+ get_date_logging()+"] " + message + '\n')

    def error(self, message):
        print(Fore.RED + "["+ get_date_logging()+"] " + message)
        if (self.logToTxt):
            self.write2file("["+ get_date_logging()+"] " + "ERROR: " + message + '\n')

    def status(self, message):
        print(Fore.MAGENTA + "["+ get_date_logging()+"] " + message)
        if (self.logToTxt):
            self.write2file("["+ get_date_logging()+"] " + "STATUS: " + message + '\n')
