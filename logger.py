import loglevel as LOGLEVEL

def create_logger(loglevel : LOGLEVEL):
    return __Logger(loglevel)

class __Logger:
    def __init__(self, loglevel):
        self.loglevel = loglevel

    def info(self, msg):
        if self.loglevel <= LOGLEVEL.INFO:
            print("[INFO] " + msg)

    def warning(self, msg):
        if self.loglevel <= LOGLEVEL.WARNING:
            print("[WARNING] " + msg)

    def debug(self, msg):
        if self.loglevel <= LOGLEVEL.DEBUG:
            print("[DEBUG] " + msg)

    def error(self, msg):
        if self.loglevel <= LOGLEVEL.ERROR:
            print("[ERROR] " + msg)

    def critical(self, msg):
        if self.loglevel <= LOGLEVEL.CRITICAL:
            print("[CRITICAL] " + msg)

