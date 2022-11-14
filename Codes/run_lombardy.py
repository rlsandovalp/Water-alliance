from parflow import Run
import os

Lombardy = Run("Lombardy", __file__)

#-----------------------------------------------------------------------------
# Set Processor topology
#-----------------------------------------------------------------------------
Lombardy.Process.Topology.P = 1
Lombardy.Process.Topology.Q = 1
Lombardy.Process.Topology.R = 1

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
Lombardy.ComputationalGrid.Lower.X = 0.0
Lombardy.ComputationalGrid.Lower.Y = 0.0
Lombardy.ComputationalGrid.Lower.Z = 0.0

Lombardy.ComputationalGrid.DX = 1000.0
Lombardy.ComputationalGrid.DY = 1000.0
Lombardy.ComputationalGrid.DZ = 100.0

Lombardy.ComputationalGrid.NX = 206
Lombardy.ComputationalGrid.NY = 194
Lombardy.ComputationalGrid.NZ = 5


#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------

Lombardy.GeomInput.Names = 'domaininput'

Lombardy.GeomInput.domaininput.GeomName = 'domain'
Lombardy.GeomInput.domaininput.GeomNames = 'domain'

Lombardy.GeomInput.domaininput.InputType = 'SolidFile'
Lombardy.GeomInput.domaininput.FileName =  '../Outputs/Lom_mask_tfg.pfsol'
Lombardy.Geom.domain.Patches =            'Bottom Top' 

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

Lombardy.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------


Lombardy.Geom.Perm.Names = 'domain'

Lombardy.Geom.domain.Perm.Type = 'Constant'
Lombardy.Geom.domain.Perm.Value = 0.1

Lombardy.Perm.TensorType = 'TensorByGeom'
Lombardy.Geom.Perm.TensorByGeom.Names = 'domain'
Lombardy.Geom.domain.Perm.TensorValX = 1.0
Lombardy.Geom.domain.Perm.TensorValY = 1.0
Lombardy.Geom.domain.Perm.TensorValZ = 0.1


#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

Lombardy.SpecificStorage.Type = 'Constant'
Lombardy.SpecificStorage.GeomNames = 'domain'
Lombardy.Geom.domain.SpecificStorage.Value = 1.0e-5

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

Lombardy.Phase.Names = 'water'

Lombardy.Phase.water.Density.Type = 'Constant'
Lombardy.Phase.water.Density.Value = 1.0
Lombardy.Phase.water.Viscosity.Type = 'Constant'
Lombardy.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

Lombardy.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------

Lombardy.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

Lombardy.Gravity = 1.0

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------
Lombardy.Geom.Porosity.GeomNames = 'domain'

Lombardy.Geom.domain.Porosity.Type = 'Constant'
Lombardy.Geom.domain.Porosity.Value = 0.3

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------
Lombardy.Phase.RelPerm.Type = 'VanGenuchten'
Lombardy.Phase.RelPerm.GeomNames = 'domain'

Lombardy.Geom.domain.RelPerm.Alpha = 3.548
Lombardy.Geom.domain.RelPerm.N = 4.162

#-----------------------------------------------------------------------------
# Saturation
#-----------------------------------------------------------------------------
Lombardy.Phase.Saturation.Type = 'VanGenuchten'
Lombardy.Phase.Saturation.GeomNames = 'domain'

Lombardy.Geom.domain.Saturation.Alpha = 3.548
Lombardy.Geom.domain.Saturation.N = 4.162
Lombardy.Geom.domain.Saturation.SRes = 0.05
Lombardy.Geom.domain.Saturation.SSat = 1.0

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

Lombardy.Mannings.Type = 'Constant'
Lombardy.Mannings.GeomNames = 'domain'
Lombardy.Mannings.Geom.domain.Value = 1e-5
#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
Lombardy.Wells.Names = ''

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------
# The UNITS on this simulation are HOURS

Lombardy.TimingInfo.BaseUnit = 1
Lombardy.TimingInfo.StartCount = 0
Lombardy.TimingInfo.StartTime = 0.0
Lombardy.TimingInfo.StopTime = 1.0
Lombardy.TimingInfo.DumpInterval = 1.0
Lombardy.TimeStep.Type = 'Constant'
Lombardy.TimeStep.Value = 1.0

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
Lombardy.Cycle.Names = 'constant'
Lombardy.Cycle.constant.Names = 'alltime'
Lombardy.Cycle.constant.alltime.Length = 1
Lombardy.Cycle.constant.Repeat = -1
#  
#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
Lombardy.BCPressure.PatchNames = 'Top'

Lombardy.Patch.Top.BCPressure.Type = 'FluxConst'
Lombardy.Patch.Top.BCPressure.Cycle = 'constant'
Lombardy.Patch.Top.BCPressure.alltime.Value = 0.0

#---------------------------------------------------------
# Topo slopes
#---------------------------------------------------------
os.system('cp Source/Lom_DEM.pfb Source/Top_Surf.pfb')
Lombardy.pfset(key='TopoSlopes.Elevation.FileName', value='../Source/Top_Surf.pfb')
Lombardy.dist('../Source/Top_Surf.pfb')

# Lombardy.pfset(key='pfslopex', value='../Source/Lom_DEM.pfb')
# Lombardy.write(file_name='Source/slope_xxx.pfb', file_format='pfb')

Lombardy.TopoSlopesX.Type = 'PFBFile'
Lombardy.TopoSlopesX.GeomNames = 'domain'
Lombardy.TopoSlopesX.FileName = '../Source/slope_x.pfb'
Lombardy.dist('../Source/slope_x.pfb')

# bbb = Lombardy.pfset(key='pfslopex', value='../Source/Lom_DEM.pfb')
# bbb.write(file_name='Source/slope_xxx.pfb', file_format='pfb')

Lombardy.TopoSlopesY.Type = 'PFBFile'
Lombardy.TopoSlopesY.GeomNames = 'domain'
Lombardy.TopoSlopesY.FileName = '../Source/slope_y.pfb'
Lombardy.dist('../Source/slope_y.pfb')

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

Lombardy.PhaseSources.water.Type = 'Constant'
Lombardy.PhaseSources.water.GeomNames = 'domain'
Lombardy.PhaseSources.water.Geom.domain.Value = 0.0

#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

Lombardy.KnownSolution = 'NoKnownSolution'

#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------

Lombardy.Solver = 'Richards'
# pfset Solver.MaxIter                                     2000000

Lombardy.Solver.Nonlinear.EtaChoice = 'Walker1'
Lombardy.Solver.Nonlinear.UseJacobian = True
Lombardy.Solver.Nonlinear.Globalization = 'LineSearch'
Lombardy.Solver.Linear.MaxRestart = 4
Lombardy.Solver.MaxConvergenceFailures = 4

Lombardy.Solver.Nonlinear.ResidualTol = 1.0e-8
Lombardy.Solver.Nonlinear.StepTol = 1e-12
Lombardy.Solver.Nonlinear.MaxIter = 150
Lombardy.Solver.Linear.KrylovDimension = 100


# pfset Solver.Linear.Preconditioner                       PFMGOctree
Lombardy.Solver.Linear.Preconditioner = 'PFMG'
Lombardy.Solver.Linear.Preconditioner.PCMatrixType = 'FullJacobian'
Lombardy.Solver.Nonlinear.PrintFlag = 'LowVerbosity'

Lombardy.Solver.PrintSubsurf = True
#pfset Solver.PrintSaturation                            False
Lombardy.Solver.Drop = 1E-15

Lombardy.Solver.TerrainFollowingGrid = True
#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

Lombardy.ICPressure.Type = 'HydroStaticPatch'
Lombardy.ICPressure.GeomNames = 'domain'
Lombardy.Geom.domain.ICPressure.Value = 0.0
Lombardy.Geom.domain.ICPressure.RefGeom = 'domain'
Lombardy.Geom.domain.ICPressure.RefPatch = 'Bottom'

#-----------------------------------------------------------------------------
# Run that puppy
#-----------------------------------------------------------------------------

Lombardy.run()