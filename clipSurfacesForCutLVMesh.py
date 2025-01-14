#coding=utf8

########################################################################
###                                                                  ###
### Created by Martin Genet, 2012-2016                               ###
###                                                                  ###
### University of California at San Francisco (UCSF), USA            ###
### Swiss Federal Institute of Technology (ETH), Zurich, Switzerland ###
### École Polytechnique, Palaiseau, France                           ###
###                                                                  ###
########################################################################

import vtk

import myVTKPythonLibrary as myVTK
from mat_vec_tools import *

########################################################################

def clipSurfacesForCutLVMesh(
        endo,
        epi,
        height,
        verbose=1):

    myVTK.myPrint(verbose, "*** clipSurfacesForCutLVMesh ***")

    plane = vtk.vtkPlane()
    plane.SetNormal(0,0,-1)
    plane.SetOrigin(0,0,height)

    clip = vtk.vtkClipPolyData()
    clip.SetClipFunction(plane)
    if (vtk.vtkVersion.GetVTKMajorVersion() >= 6):
        clip.SetInputData(endo)
    else:
        clip.SetInput(endo)
    clip.Update()
    clipped_endo = clip.GetOutput(0)

    clip = vtk.vtkClipPolyData()
    clip.SetClipFunction(plane)
    if (vtk.vtkVersion.GetVTKMajorVersion() >= 6):
        clip.SetInputData(epi)
    else:
        clip.SetInput(epi)
    clip.Update()
    clipped_epi = clip.GetOutput(0)

    return (clipped_endo,
            clipped_epi)

