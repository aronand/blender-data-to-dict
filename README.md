# blender-data-to-json
Output a number of different information about the contents of a Blender 3D file into a JSON file.

**Note that as of now there are no plans to dump any of the 3D data.**

## Planned output contents

Each listed key will hold a dictionary where a corresponding data type's contents can be found using its name. In other words, using `json["objects"]["Cube"]` will give access to data equivalent to using `bpy.data.objects["Cube"]`.

- objects
- meshes
- materials
- images

## How to use

Currently the only way to use the script is either by passing it to Blender through command line, or by using the script through Blender's script editor.

## Why

The idea for the tool originates from another project where an n amount of data reading scripts would be run in Blender. Instead of opening Blender n amount of times, this tool would allow dumping all the needed data out of Blender in a single go.

The idea is not to dump absolutely everything, but merely the easier to access parts for now.
