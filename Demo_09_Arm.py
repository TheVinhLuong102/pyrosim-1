from pyrosim import PYROSIM

# Constants

ARM_LENGTH = 0.5

ARM_RADIUS = ARM_LENGTH / 10.0

sim = PYROSIM(playPaused = True , evalTime = 1000)

# Upper arm

sim.Send_Cylinder(ID = 0 , x=0, y=0, z=ARM_LENGTH/2.0 + ARM_RADIUS, r1=0, r2=0, r3=1, length=ARM_LENGTH, radius=ARM_RADIUS)

# Lower arm

sim.Send_Cylinder(ID = 1 , x=0, y=ARM_LENGTH/2.0, z=ARM_LENGTH + ARM_RADIUS, r1=0, r2=1, r3=0, length=ARM_LENGTH, radius=ARM_RADIUS)


sim.Start()
