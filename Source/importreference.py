import os
import math
import bpy

basedir = r"C:\your\path\to\extracted\data\"
reference = "filenameOfRef.txt"
objdata = "objdata.txt"


attrs = {}
for line in open(os.path.join(basedir, reference)):
    elements = line[1:].split()
    if len(elements) == 8:
        attrs[elements[0]] = elements[1:]

pathmap = {}
for line in open(os.path.join(basedir, objdata)):
    elements = line.split("\t")
    if len(elements) == 8 and elements[4].endswith(".nif"):
        pathmap[elements[0]]= elements[4]

for attr in attrs:
    name = attr[:-3]
    if name in pathmap:
        floats = [float(s) for s in attrs[attr]]
        old_objects = {obj for obj in bpy.data.objects}
        bpy.ops.import_scene.pynifly(filepath=os.path.join(os.path.join(basedir, "Meshes"), pathmap[name]))
        new_objects = {obj for obj in bpy.data.objects}
        added_objects = new_objects.difference(old_objects)
        print(name, "attributes are", attrs[attr])
        for obj in added_objects:
            print(" ", obj.name)
            obj.location = floats[:3]
            obj.rotation_euler = [math.radians(angle) for angle in floats[3:6]]
            scale = floats[6]
            obj.scale = (scale, scale, scale)
