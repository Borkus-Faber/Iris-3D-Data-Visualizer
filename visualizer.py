import bpy
import csv
import os

# clear scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# setup colors
red = bpy.data.materials.new(name="setosa_red")
red.diffuse_color = (0.8, 0.1, 0.1, 1)
green = bpy.data.materials.new(name="versicolor_green")
green.diffuse_color = (0.1, 0.8, 0.1, 1)

blue = bpy.data.materials.new(name="virginica_blue")
blue.diffuse_color = (0.1, 0.1, 0.8, 1)
dataset_file = r"C:\Users\mathe\Documents\Iris Data\Iris.csv"

# check if the file exists
assert os.path.exists(dataset_file), "cant find the file"

f = open(dataset_file, 'r')
reader = csv.reader(f)
row_counter = 0

for row in reader:
    if row_counter > 0:
        
        # check if there's at least 6 columns
        assert len(row) >= 6, "missing data in row"
        
        # columns for xyz coordinates
        x = float(row[1]) 
        y = float(row[2]) 
        z = float(row[3]) 
        
        # check flower length if negative
        assert x > 0 and y > 0 and z > 0, "bad measurement data"
        
        species = row[5] 
        
        # 
        bpy.ops.mesh.primitive_cube_add(size=0.15, location=(x, y, z))
        cube = bpy.context.active_object
        
        # color based on species type
        if species == "Iris-setosa":
            cube.data.materials.append(red)
        elif species == "Iris-versicolor":
            cube.data.materials.append(green)
        else:
            cube.data.materials.append(blue)
            
        cube.name = "Flower_" + str(row_counter)

    row_counter = row_counter + 1

f.close()
# check if the dataset file is empty
assert row_counter > 1, "dataset is empty"

print("Done")
