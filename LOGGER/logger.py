
import logging

logpath = "./"
# logpath = "."
logfile = "mqttlib.log"
loglevel = logging.INFO # SET DESIRED LEVEL



def set_logger(logfile, loglevel=logging.WARNING):
    """ === Python LOGGING """
    # loglevel = logging.INFO  # adjust as desired
    dtfmt = "%Y-%m-%d %H:%M:%S"  # date/time format
    logfmt = "%(levelname)s: %(asctime)s: %(message)s"  # logging format
    logging.basicConfig(filename=logfile,
                        level=loglevel,
                        format=logfmt,
                        datefmt=dtfmt)
    return logging.getLogger()  # end method and return logger instance

logger = set_logger(logpath + "/" + logfile, loglevel)