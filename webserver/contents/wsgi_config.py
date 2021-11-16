import multiprocessing

from contents.config import Config


def app_config():
    return Config()


bind = str(app_config().get("webserver", "host") + ":"
           + str(app_config().get("webserver", "port")))

workers = 1
threads = 2 * multiprocessing.cpu_count() + 1

proc_name = str(app_config().get("webserver", "process_name"))
