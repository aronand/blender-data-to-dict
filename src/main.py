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
        self.materials: dict[str, Any] = {}
        self.images: dict[str, Any] = {}

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
        from blenderdatadict import BlenderDataDict

        logging.info("Getting objects")
        for obj in bpy.data.objects:
            logging.debug(f"Adding object '{obj.name}'")
            self.objects |= BlenderDataDict.get_dict(obj)

        logging.info("Getting meshes")
        for mesh in bpy.data.meshes:
            logging.debug(f"Adding mesh '{mesh.name}'")
            self.meshes |= BlenderDataDict.get_dict(mesh)

        logging.info("Getting materials")
        for material in bpy.data.materials:
            logging.debug(f"Adding material '{material.name}'")
            self.materials |= BlenderDataDict.get_dict(material)

        logging.info("Getting images")
        for image in bpy.data.images:
            logging.debug(f"Adding image '{image.name}'")
            self.images |= BlenderDataDict.get_dict(image)

        json_path: str = os.path.join(self.root, "output.json")
        json_contents: dict[str, dict] = {
            "objects": self.objects,
            "meshes": self.meshes,
            "materials": self.materials,
            "images": self.images
        }
        logging.info(f"Writing contents to {json_path}")
        with open(json_path, "w") as output:
            json.dump(json_contents, output, indent=2)


if __name__ == "__main__":
    start_time: float = time.perf_counter()
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s: %(levelname)s - %(message)s")
    logging.info("Starting script")
    Main().run()
    elapsed_time: float = time.perf_counter() - start_time
    logging.info(f"Took {elapsed_time:0.2f} seconds")

