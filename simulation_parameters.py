import numpy as np 

# Structure of the simulation 
myfile0_title = "./parameters/structure.txt"
myfile0 = open(myfile0_title,"w")
dimension = 2 # (1, 2, 3) : Dimensions accepted for the simulation 
myfile0.write("dimension"+"\t"+str(dimension)+"\n")
myfile0.close()
# ----------------------------------------------------------------

# Outputs 
myfile1_title = "./parameters/outputs.txt"
myfile1 = open(myfile1_title, "w")
output_name_prefix = "body" # example : body_450.dat 
myfile1.write("output_name_prefix"+"\t"+str(output_name_prefix)+"\n")
output_name_postfix = "" # example : body_450_heavy.dat 
myfile1.write("output_name_postfix"+"\t"+str(output_name_postfix)+"\n")
output_name_ext = "dat" # txt, dat, out ... 
myfile1.write("output_name_ext"+"\t"+str(output_name_ext)+"\n")
output_type = "one_by_body" # Output types  
myfile1.write("output_type"+"\t"+str(output_type)+"\n")
myfile1.close()
# ----------------------------------------------------------------

# Main parameters
myfile2_title = "./parameters/main_parameters.txt"
myfile2 = open(myfile2_title,"w")
num_bodies = 50 # (1, ...) : Number of bodies in the simulation 
myfile2.write("num_bodies"+"\t"+str(num_bodies)+"\n")

body_mass_distribution = "no" # If you want a specific mass distribution 
myfile2.write("body_mass_distribution"+"\t"+str(body_mass_distribution)+"\n")
normalized_mass = 1  # Normalized mass value of bodies 
myfile2.write("normalized_mass"+"\t"+str(normalized_mass)+"\n")
if (body_mass_distribution == "yes") : 
    mass_distribution = "test_distribution" # Example of mass distribution 
    myfile2.write("mass_distribution"+"\t"+str(mass_distribution)+"\n")

body_radius_distribution = "no" # If you want a specific radius distribution 
myfile2.write("body_radius_distribution"+"\t"+str(body_radius_distribution)+"\n")
normalized_radius = 1 # Normalized radius value of bodies 
myfile2.write("normalized_radius"+"\t"+str(normalized_radius)+"\n")
if (body_radius_distribution == "yes") : 
    radius_distribution = "test_distribution" # Example of radius distribution 
    myfile2.write("radius_distribution"+"\t"+str(radius_distribution)+"\n")

body_position_distribution = "uniform_rectangle" # Initial position distribution
myfile2.write("body_position_distribution"+"\t"+str(body_position_distribution)+"\n")
body_velocity_distribution = "uniform_rectangle" # Initial velocity distribution
myfile2.write("body_velocity_distribution"+"\t"+str(body_velocity_distribution)+"\n")

softening = 1e-2 # Parameter allowing to avoid numerical divergences 
myfile2.write("softening"+"\t"+str(softening)+"\n")

collisions = "no" # Solid collisions between bodies 
myfile2.write("collisions"+"\t"+str(collisions)+"\n")
if (collisions == "yes") : 
    collision_consequence = "fusion" # Example of consequence of a collision between two bodies
    myfile2.write("collision_consequence"+"\t"+str(collision_consequence)+"\n") 


viscosity = "no" # Presence of a gas 
myfile2.write("viscosity"+"\t"+str(viscosity)+"\n")
if (viscosity == "yes") : 
    viscosity_law = "exmaple" # Example of law of viscosity 
    myfile2.write("viscosity_law"+"\t"+str(viscosity_law)+"\n")

time_initial = 0. # Time at which the simulation begin 
myfile2.write("time_initial"+"\t"+str(time_initial)+"\n")
time_final = 100. # Time at which the simulation end 
myfile2.write("time_final"+"\t"+str(time_final)+"\n")
variable_step = "no"
myfile2.write("variable_step"+"\t"+str(variable_step)+"\n")
step_min = 1e-2 # Example of step (min value for variable step, fixed value for fixed step)
myfile2.write("step_min"+"\t"+str(step_min)+"\n")
if (variable_step == "yes") : 
    step_rule = "exmaple" # Example of rule for a variable step
    myfile2.write("step_rule"+"\t"+str(step_rule)+"\n")
myfile2.close()
# ----------------------------------------------------------------

# Optimization and solving parameters 
myfile3_title = "./parameters/opt_solve.txt"
myfile3 = open(myfile3_title,"w")
barnes_hut = "no" # Barnes-hut optimization method
myfile3.write("barnes_hut"+"\t"+str(barnes_hut)+"\n")
sph = "no" # Smooth-particle-hydrodynamics grid 
myfile3.write("sph"+"\t"+str(sph)+"\n")
solver = "verlet" # Brut-force solver
myfile3.write("solver"+"\t"+str(solver)+"\n")
myfile3.close()
# ----------------------------------------------------------------




