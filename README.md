# blender-data-to-json
Output a number of different information about the contents of a Blender 3D file into a JSON file.

## Planned output contents

Each listed key will hold a dictionary where a corresponding data type's contents can be found using its name. In other words, using `json["objects"]["Cube"]` will give access to data equivalent to using `bpy.data.objects["Cube"]`.

- objects
- meshes
- materials
- images

## How to use

Currently the only way to use the script is either by passing it to Blender through command line, or by using the script through Blender's script editor.
