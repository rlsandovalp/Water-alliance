lappend auto_path $env(PARFLOW_DIR)/bin 
package require parflow
namespace import Parflow::*

# # ----- First we'll build the domain mask -----
set DEM [pfload -pfb "Source/Lom_DEM.pfb"]
set Mask [pfload -pfb "Source/Lom_Mask.pfb"]
set DMsk [pfload -pfb "Source/Lom_Dummy_Mask.pfb"]
set Bot [pfcellsumconst $DEM -500 $DMsk]

# Now transform it to be a TFG solid
set Top [pfcelldiff $DEM $DEM $DMsk]
set Bot [pfcelldiff $Bot $DEM $DMsk]
set Top [pfcellsumconst  $Top 500 $DMsk]
set Bot [pfcellsumconst  $Bot 500 $DMsk]
pfpatchysolid -top $Top -bot $Bot -pfsol "Outputs/Lom_mask_tfg.pfsol" -msk $Mask -vtk "Outputs/Lom_mask_tfg.vtk"

#---------------------------------------------------------
# Topo slopes
#---------------------------------------------------------

pfsave [pfslopex $DEM] -pfb "Source/slope_x.pfb"
pfsave [pfslopey $DEM] -pfb "Source/slope_y.pfb"
