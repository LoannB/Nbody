
# Suppression de toutes les données des simulations précédentes 
cd ../out
rm body*
cd ../bin/

# Execution du fichier de pointage des paramètres de la simulation
cd ..
python ./simulation_parameters.py

# Execution du script de génération de la distribution de masses
cd ../tools/
python ./distribution_generator.py
cd ../bin/

# Compilation du code 
g++ -std=c++11 ../src/main.cpp -o main.o
./main.o

