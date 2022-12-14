# blender-data-to-dict
Output a number of different information about the contents of a Blender scene into a dictionary.

**Note that as of now there are no plans to dump any of the 3D data.**

## Why

The idea for the script originates from another project where an n amount of data reading scripts would be run in
Blender. Instead of opening Blender n amount of times, this script could be used to dump all the necessary data in a
single step.

Its usefulness is to be decided. For now, it's an interesting way to get more familiar with Blender's internals.

## Planned output contents

Each listed key will hold a dictionary where a corresponding data type's contents can be found using its name. In other
words, using `dict["objects"]["Cube"]` will give access to data equivalent to using `bpy.data.objects["Cube"]`.

- objects
- meshes
- materials
- images

## Minimum Python and Blender version

The script uses union type annotation introduced in Python 3.10, making [Blender 3.1](https://wiki.blender.org/wiki/Reference/Release_Notes/3.1/Python_API)
the oldest supported version as is.

## How to use

Incorporate the BlenderData class from blenderdata.py into your script, or use the script as is, but change the code so as to call BlenderData during execution.

To generate the dictionary:
```python
data: dict[str, Any] = BlenderData.dict()
```
