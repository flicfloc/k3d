#python

import k3d
import testing

document = k3d.new_document()

grid = document.new_node("PolyGrid");
grid.columns = 1
grid.rows = 1

modifier = document.new_node("SubdivideEdges")
cuda_modifier = document.new_node("CUDASubdivideEdges")

modifier.mesh_selection = k3d.geometry.selection.create(1)
modifier.vertices = 1

cuda_modifier.mesh_selection = modifier.mesh_selection
cuda_modifier.vertices = 1

document.set_dependency(modifier.get_property("input_mesh"), grid.get_property("output_mesh"))
document.set_dependency(cuda_modifier.get_property("input_mesh"), grid.get_property("output_mesh"))

testing.output_mesh_difference(cuda_modifier.output_mesh, modifier.output_mesh, 1)

difference = testing.get_mesh_difference(document, cuda_modifier.get_property("output_mesh"), modifier.get_property("output_mesh"), 1)

if not difference.equal:
    raise "Meshes not equal"