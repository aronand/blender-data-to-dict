import bpy
import json
import logging
import os.path
import sys
import time
from typing import Any


class Main:
    def __init__(self):
        self.__root: str | None = None  # Use the property and the setter instead of directly accessing
        self.objects: dict[str, Any] = {}

    @property
    def root(self) -> str:
        return self.__root

    @root.setter
    def root(self, path: str):
        if not os.path.isdir(path):
            raise FileNotFoundError(f"Couldn't set root path, {path} not found")
        self.__root = path

    def __get_root_path(self):
        """Gets the root path from args and appends it to sys.path"""
        idx: int = sys.argv.index("--")
        self.root = sys.argv[idx + 1]  # TODO: Use argparse instead if possible?
        logging.debug(f"Root path is {self.root}")
        sys.path.append(self.root)

    def run(self):
        self.__get_root_path()
        from blenderdata import blender_object_generator

        for obj in blender_object_generator(bpy.data.objects):
            obj_dict: dict[str, Any] = obj.dict
            obj_name: str = list(obj_dict.keys())[0]
            logging.debug(f"Adding object '{obj_name}'")
            self.objects |= obj_dict

        json_path: str = os.path.join(self.root, "output.json")
        json_contents: dict[str, dict] = {"objects": self.objects}
        logging.debug(f"Writing contents to {json_path}")
        with open(json_path, "w") as output:
            json.dump(json_contents, output, indent=2)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s: %(levelname)s - %(message)s")
    logging.debug("Starting script")
    Main().run()
