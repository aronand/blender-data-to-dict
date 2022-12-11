import bpy
import json
import os.path
import sys
from typing import Any


def main(root_path: str):
    from blenderdata import blender_object_generator

    objects_dict: dict[str, Any] = {}
    for obj in blender_object_generator(bpy.data.objects):
        objects_dict |= obj.dict

    json_contents: dict[str, dict] = {"objects": objects_dict}
    with open(os.path.join(root_path, "output.json"), "w") as output:
        json.dump(json_contents, output, indent=2)


if __name__ == "__main__":
    idx: int = sys.argv.index("--")
    root: str = sys.argv[idx + 1]
    sys.path.append(root)
    main(root)
