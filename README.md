# blender-data-to-dict
Output a number of different information about the contents of a Blender scene into a dictionary.

**Note that as of now there are no plans to dump any of the 3D data.**

## Why

The idea for the script originates from another project where an n amount of data reading scripts would be run in
Blender. Instead of opening Blender n amount of times, this script could be used to dump all the necessary data in a
single step.

Its usefulness is to be decided. For now, it's an interesting way to get more familiar with Blender's internals.

## Output contents

Each listed key will hold a dictionary where a corresponding data type's contents can be found using its name. In other
words, using `dict["objects"]["Cube"]` will give access to data equivalent to using `bpy.data.objects["Cube"]`.

<details>
<summary>images</summary>

- channels: <sup><sub>int</sup></sub>
- depth: <sup><sub>int</sup></sub>
- file_format: <sup><sub>str</sup></sub>
- filepath: <sup><sub>str</sup></sub>
- size: <sup><sub>tuple[int, int]</sup></sub>
- source: <sup><sub>str</sup></sub>
- type: <sup><sub>str</sup></sub>
</details>

<details>
<summary>materials</summary>

- node_tree: <sup><sub>dict[str, dict]</sup></sub>
  - nodes: <sup><sub>dict[str, Any]</sup></sub>
    - type: <sup><sub>str</sup></sub>
    - image: <sup><sub>str | None</sup></sub> (*name of the image if not None and node is instance of ShaderNodeTexImage*)
</details>

<details>
<summary>meshes</summary>

- edges: <sup><sub>int</sup></sub>
- loops: <sup><sub>int</sup></sub>
- polygons: <sup><sub>int</sup></sub>
- loop_triangles: <sup><sub>int</sup></sub>
- vertices: <sup><sub>int</sup></sub>
</details>

<details>
<summary>objects</summary>

- data: <sup><sub>str | None</sup></sub> (*name of data object (e.g. mesh) if not None*)
- material_slots: <sup><sub>list[str]</sup></sub> (*names of materials used by objects, if any*)
- modifiers: <sup><sub>list[str]</sup></sub> (*types of (unapplied) modifiers the object has, if any*)
- type: <sup><sub>str</sup></sub> (*the type of the object, e.g. "MESH"*)
</details>

<details>
<summary>scenes</summary>

- objects: <sup><sub>list[str]</sup></sub> (*names of objects in scene, if any*)
- view_layers: <sup><sub>list[str]</sup></sub> (*names of scene view layers*)
</details>

## Minimum Python and Blender version

The script uses union type annotation introduced in Python 3.10, making
[Blender 3.1](https://wiki.blender.org/wiki/Reference/Release_Notes/3.1/Python_API) the oldest supported version without
modifications.

## How to use

Incorporate the BlenderData class from blenderdata.py into your script, or use the script as is, but change the code to
call BlenderData during execution.

### Generating the dictionary

```python
data: dict[str, Any] = BlenderData.dict()
```

### Calculating scene triangles

```python
scenes: dict[str, Any] = data["scenes"]
objects: dict[str, Any] = data["objects"]
meshes: dict[str, Any] = data["meshes"]

for scene, contents in scenes.items():
    tris: int = 0
    for obj in contents["objects"]:
        if objects[obj]["type"] != "MESH":
            continue
        mesh: str = objects[obj]["data"]
        tris += meshes[mesh]["loop_triangles"]
    print(f"Scene \"{scene}\" tris: {tris}")
```

> Note that this works for other scene data as well (vertices, edges, faces)

