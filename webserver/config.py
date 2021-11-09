from envyaml import EnvYAML
import os


class Config:

    ROOT_DIR = os.path.dirname(__file__)
    CONFIG_FILE = "resources/config.yml"

    def __init__(self):
        self.config = EnvYAML(Config.relative_directory(Config.CONFIG_FILE))

    def get(self, group: str, key: str):
        return self.config[group][key]

    @staticmethod
    def relative_directory(path: str):
        return os.path.join(Config.ROOT_DIR, path)
