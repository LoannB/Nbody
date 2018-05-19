#include <iostream> //For console output/input
#include <fstream>  //Allows to read/write files 
#include <math.h>   //Basic mathematic functions 
#include <vector>   //For dynamic arrays 
#include <string>   //Operations on strings 
#include <tuple>
#include <cmath>
#include <sstream>
using namespace std;


class body 
{
    public : 

    body(){};
    double read_mass(); 
    double read_x();
    double read_y();
    double read_vx();
    double read_vy();
    double read_ax();
    double read_ay();
    void edit_mass(double m); 
    void edit_position(double xnew, double ynew);
    void edit_velocity(double vxnew, double vynew); 
    void edit_acceleration(double axnew, double aynew);
    void action_potential(body objet); 
    void reset_potential();
    void euler(double dt);
    void verlet_2step(int step, double dt, double ax0, double ay0);

    private : 

    double mass;
    double rx;
    double ry;
    double vx;
    double vy;
    double ax;
    double ay;
};


double body::read_mass() 
{
    return mass;
}

double body::read_x()
{
    return rx;
}

double body::read_y()
{
    return ry;
}

double body::read_vx()
{
    return vx;
}

double body::read_vy()
{
    return vy;
}

double body::read_ax()
{
    return ax;
}

double body::read_ay()
{
    return ay;
}

void body::edit_mass(double m)
{
    mass = m;
}

void body::edit_position(double xnew, double ynew)
{
    rx = xnew;
    ry = ynew;
}

void body::edit_velocity(double vxnew, double vynew)
{
    vx = vxnew;
    vy = vynew;
}

void body::edit_acceleration(double axnew, double aynew)
{
    ax = axnew;
    ay = aynew;
}

void body::action_potential(body objet)
{
        double eps = 1e-2; // Softening factor
        double distance = sqrt(pow(rx - objet.read_x(),2) + pow(ry - objet.read_y(),2)) + eps; 
        double G = 1; 
        ax +=  G*objet.read_mass()*(objet.read_x()-rx)/pow(distance,2.);
        ay +=  G*objet.read_mass()*(objet.read_y()-ry)/pow(distance,2.);

}

void body::reset_potential()
{ 
    ax = 0;
    ay = 0;
}

void body::euler(double dt)
{
    vx = vx + dt*ax;
    vy = vy + dt*ay;
    rx = rx + dt*vx + 0.5*pow(dt,2)*ax;
    ry = ry + dt*vy + 0.5*pow(dt,2)*ay; 
}

void body::verlet_2step(int step, double dt, double ax0, double ay0)
{
    if (step == 1)
    {
        rx = rx + vx*dt + 0.5*pow(dt, 2.)*ax;
        ry = ry + vy*dt + 0.5*pow(dt, 2.)*ay;
    }

    if (step ==2)
    {
        vx = vx + 0.5*dt*(ax0 + ax);
        vy = vy + 0.5*dt*(ay0 + ay); 
    }
}