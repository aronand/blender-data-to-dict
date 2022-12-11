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
        self.meshes: dict[str, Any] = {}

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
        from blenderdata import BlenderDataFactory, BlenderObject

        for obj in bpy.data.objects:
            logging.debug(f"Adding object '{obj.name}'")
            bd_obj: BlenderObject = BlenderDataFactory.get_blender_object(obj)
            self.objects |= bd_obj.dict
            if obj.type != "MESH":
                continue
            self.meshes |= bd_obj.data.dict

        json_path: str = os.path.join(self.root, "output.json")
        json_contents: dict[str, dict] = {
            "objects": self.objects,
            "meshes": self.meshes
        }
        logging.debug(f"Writing contents to {json_path}")
        with open(json_path, "w") as output:
            json.dump(json_contents, output, indent=2)


if __name__ == "__main__":
    start_time: float = time.perf_counter()
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s: %(levelname)s - %(message)s")
    logging.debug("Starting script")
    Main().run()
    elapsed_time: float = time.perf_counter() - start_time
    logging.debug(f"Took {elapsed_time:0.2f} seconds")

