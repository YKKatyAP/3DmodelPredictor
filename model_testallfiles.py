import trimesh
from trimesh import creation
import numpy as np
import os
import matplotlib as mplot
import csv

#KATY: go back and optimize, should be a function call

output_List = []
#outputList_ = []

# iterating through every model
refModelFolder = 'recognition_models/final_mods'
for file in os.listdir(refModelFolder):
    filepath = os.path.join(refModelFolder, file)
    print(filepath, "!!!!!")

    # output lists for each dimension of model
    outputX = []
    outputX.append("X" + file)
    outputY = []
    outputY.append("Y" + file)
    outputZ = []
    outputZ.append("Z" + file)
    
    mesh = trimesh.load(filepath)
    bounds = mesh.bounds

    # get all values in space between the upper and lower bounds of the model
    cutArr_x = np.linspace(bounds[0][2], bounds[1][2], 20)
    cutArr_y = np.linspace(bounds[0][1], bounds[1][1], 20)
    cutArr_z = np.linspace(bounds[0][0], bounds[1][0], 20)

    counter = 1

    # take the area of every cross-section and the cross-section following it, find ratio
    for i in range(len(cutArr_x)-2):
        print(counter)
        counter += 1

        # ------- X cross-section --------

        plane_normal_x = np.array([1, 0, 0])
        plane_origin_x = np.array([cutArr_x[i], 0, 0])
        plane_origin_xNext = np.array([cutArr_x[i + 1], 0, 0])



        """cross_Section_x = mesh.section(plane_normal_x, plane_origin_x)
        cross_SectionNext_x = mesh.section(plane_normal_x, plane_origin_xNext)
        cross_Planar_x, matr_x = cross_Section_x.to_planar()
        cross_PlanarNext_x, matrNext_x = cross_SectionNext_x.to_planar()
    

        area_x = cross_Planar_x.area
        areaNext_x  = cross_PlanarNext_x.area
        ratio_x = area_x / areaNext_x
        outputX.append(ratio_x)"""



        # ------- Y cross-section -------

        plane_normal_y = np.array([1, 0, 0])
        plane_origin_y = np.array([cutArr_y[i], 0, 0])
        plane_origin_yNext = np.array([cutArr_y[i + 1], 0, 0])

        cross_Section_y = mesh.section(plane_normal_y, plane_origin_y)
        cross_SectionNext_y = mesh.section(plane_normal_y, plane_origin_yNext)

        cross_Planar_y, matr_y = cross_Section_y.to_planar()
        cross_PlanarNext_y, matrNext_y = cross_SectionNext_y.to_planar()
    
        area_y = cross_Planar_y.area
        areaNext_y  = cross_PlanarNext_y.area
        ratio_y = area_y / areaNext_y
        outputY.append(ratio_y)

        # # # # # # # # # #
        scene = trimesh.Scene()
        scene.add_geometry(mesh)
        scene.add_geometry(cross_Planar_y)
        scene.show()
        # # # # # # # # # # 


        # ------- Z cross-section -------

        plane_normal_z = np.array([0, 0, 1])
        plane_origin_z = np.array([0, 0, cutArr_z[i]])
        plane_origin_zNext = np.array([0, 0, cutArr_z[i+1]])

        cross_Section_z = mesh.section(plane_normal_z, plane_origin_z)
        cross_SectionNext_z = mesh.section(plane_normal_z, plane_origin_zNext)      

        cross_Planar_z, matr_z = cross_Section_z.to_planar()
        cross_PlanarNext_z, matrNext_z = cross_SectionNext_z.to_planar()
    
        area_z = cross_Planar_z.area
        areaNext_z  = cross_PlanarNext_z.area
        ratio_z = area_y / areaNext_z
        outputZ.append(ratio_z)

    

print(outputX, "X-CROSS")
print(outputY, "Y-CROSS")
print(outputZ, "Z-CROSS")

output_List.append(outputX)
output_List.append(outputY)
output_List.append(outputZ)

#with open('databank.csv', 'a', newline='') as file:
#    fileWriter = csv.writer(file)
#    fileWriter.writerows(output_toFile)
    




