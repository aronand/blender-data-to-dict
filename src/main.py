import bpy
import json
import logging
import os.path
import sys
from typing import Any


def main(root_path: str):
    from blenderdata import blender_object_generator

    objects_dict: dict[str, Any] = {}
    for obj in blender_object_generator(bpy.data.objects):
        obj_dict: dict[str, Any] = obj.dict
        obj_name: str = list(obj_dict.keys())[0]
        logging.debug(f"Adding object '{obj_name}'")
        objects_dict |= obj_dict

    json_path: str = os.path.join(root_path, "output.json")
    json_contents: dict[str, dict] = {"objects": objects_dict}
    logging.debug(f"Writing contents to {json_path}")
    with open(json_path, "w") as output:
        json.dump(json_contents, output, indent=2)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Starting script")
    idx: int = sys.argv.index("--")
    root: str = sys.argv[idx + 1]
    logging.debug(f"Root path is {root}")
    sys.path.append(root)
    main(root)
