#include <iostream> //For console output/input
#include <fstream>  //Allows to read/write files 
#include <math.h>   //Basic mathematic functions 
#include <vector>   //For dynamic arrays 
#include <string>   //Operations on strings 
#include <tuple>
#include <cmath>
#include <sstream>
#include "./class/class_body.h"
using namespace std;



int main()
{
    int N = 50; 
    vector<body> objet;
    int id[N];
    double rx[N], ry[N], vx[N], vy[N];



    ifstream distrib_file;
    std::string distrib_file_name = "../dist/";
    std::string ext = ".dat";
    std::string distribution = "uniform_circle";

    distrib_file_name.append(distribution);
    distrib_file_name.append(ext);

    distrib_file.open(distrib_file_name);
    int j=0;
    while (!distrib_file.eof())
    {
        distrib_file >> id[j];
        distrib_file >> rx[j];
        distrib_file >> ry[j];
        distrib_file >> vx[j];
        distrib_file >> vy[j];
        j++;
    }

    for (int ii=0; ii<N; ii++)
    {
        double m = 1.0;
        body obj1; 
        obj1.edit_mass(m);
        obj1.edit_position(rx[ii], ry[ii]);
        obj1.edit_velocity(vx[ii], vy[ii]);
        obj1.edit_acceleration(0, 0);
        objet.push_back(obj1);
    }

    ofstream body_output[N]; 
    std::string name[N];
    for (int ii=0; ii<N; ii++)
    {
        name[ii] = "../out/body_";
        std::ostringstream number;
        number << ii;
        name[ii].append(number.str());
        std::string ext=".dat";
        name[ii].append(ext);
        body_output[ii].open(name[ii]);
    }





    double Tini = 0; 
    double dt = 1e-3; 
    double Tfin = 3.;

    double t = 0; 
    while(t < Tfin)
    {
        cout<<" Avancement : "<<t/Tfin*100.<<" %"<<endl;
        for (int ii=0; ii<N; ii++)
        {
            objet[ii].reset_potential();
            for (int jj=0; jj<N; jj++)
            {
                if (jj != ii) {objet[ii].action_potential(objet[jj]);}
            }  
            objet[ii].verlet_2step(1, dt, 0., 0.);
        }
        for (int ii=0; ii<N; ii++)
        {   
            double ax0 = objet[ii].read_ax();
            double ay0 = objet[ii].read_ay();
            objet[ii].reset_potential();
            for (int jj=0; jj<N; jj++)
            {
                if (jj != ii) {objet[ii].action_potential(objet[jj]);}
            } 
            objet[ii].verlet_2step(2, dt, ax0, ay0);
        }


        //for (int ii=0; ii<N; ii++)
        //{
        //    objet[ii].euler(dt);
        //}
        //cout<<"Position = [t = "<<t/Tfin<<"] ("<<objet[0].read_ax()<<" ,"<<objet[0].read_ay()<<")"<<endl;

        for (int ii=0; ii<N; ii++)
        {
            body_output[ii]<<t<<"\t"<<objet[ii].read_x()<<"\t"<<objet[ii].read_y();
            body_output[ii]<<"\t"<<objet[ii].read_vx()<<"\t"<<objet[ii].read_vy();
            body_output[ii]<<"\t"<<objet[ii].read_ax()<<"\t"<<objet[ii].read_ay()<<endl;
        }
        t += dt;
    }
    for (int ii=0; ii<N; ii++)
    {
        body_output[ii].close();
    }
}