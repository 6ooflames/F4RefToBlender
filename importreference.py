import os
import math
import bpy

attrs = {}
for line in open(r""):
    elements = line[1:].split()
    if len(elements) == 8:
        attrs[elements[0]] = elements[1:]

pathmap = {}
for line in open(r""):
    elements = line.split("\t")
    if len(elements) == 8 and elements[4].endswith(".nif"):
        pathmap[elements[0]]= elements[4]

for attr in attrs:
    name = attr[:-3]
    if name in pathmap:
        floats = [float(s) for s in attrs[attr]]
        old_objects = {obj for obj in bpy.data.objects}
        bpy.ops.import_scene.nifly(filepath = r"" + "\\" + pathmap[name])
        new_objects = {obj for obj in bpy.data.objects}
        added_objects = new_objects.difference(old_objects)
        print(name, "attributes are", attrs[attr])
        for obj in added_objects:
            print(" ", obj.name)
            obj.location = floats[:3]
            obj.rotation_euler = [math.radians(angle) for angle in floats[3:6]]
            scale = floats[6]
            obj.scale = (scale, scale, scale)
