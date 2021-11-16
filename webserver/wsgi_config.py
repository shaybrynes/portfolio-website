import multiprocessing

from config import Config


def app_config():
    return Config()


bind = str(app_config().get("server", "host") + ":"
           + str(app_config().get("server", "port")))

workers = 1
threads = 2 * multiprocessing.cpu_count() + 1

proc_name = str(app_config().get("server", "process_name"))
