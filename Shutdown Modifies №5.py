# __Author__ __Lencof__
# Shutdown Modifies №5.py

import os, sys, time, platform

def shutdown():
    return os.system('shutdown -s -t 0')

shutdown()


class TerminalPrinter:
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")


class FilePrinter:
    def write(self, msg):
        with open('log.json', 'a+', encoding='UTF8') as f:
            f.write(f"{msg}\n")


class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime()), platform.system()


    def log_stderr(self, message):
        TerminalPrinter().write(f"{self.prefix} {message}")


    def log_file(self, message):
        FilePrinter().write(f"{self.prefix} {message}")

    

logger = Logger()
logger.log_file("Starting OFF.py")
logger.log_stderr("An error!")
