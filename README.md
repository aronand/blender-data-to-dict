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

The tool does not work with Blender out of the box due to being broken into modules.

To run the script, pass the following arguments to Blender in command line or in shortcut:

`-b {blend_file} -P {script_path} -- {script_root}`

Everything after `--` will be  omitted by Blender and used by the script. Currently the JSON is written into the script
root.

> You can also pass `--factory-startup` to Blender to omit loading of startup scripts.

## Why

The idea for the tool originates from another project where an n amount of data reading scripts would be run in Blender. Instead of opening Blender n amount of times, this tool would allow dumping all the needed data out of Blender in a single go.

The idea is not to dump absolutely everything, but merely the easier to access parts for now.
