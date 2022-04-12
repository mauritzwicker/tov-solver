'''
name: functions
date: 27.01.2022
author: @mauritzwicker
repo: /tov-solver

Purpose: To hold tov-solver functions

'''

# Imports
import numpy as np
import math
import warnings
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pickle
import os

def check_userinput(const, defa, usr):
    '''
    function to check user inputs and assign default values

    - Inputs:
        const := constant values object
        defa := default values objects
        usr := usr values object
    - Returns:
        usr := checked/unchecked and default assigned user values
    '''

    if usr.check_inputs == False:
        print('*************************************************')
        print('\t!!!!! WARNING !!!!!')
        print('\t User has decided to not check input')
        print('\t We strongly advise against this')
        print('\t Code will likely output incorrect results')

        # Allocate values for NONE, then return
        if usr.rho_c is not None:
            usr.p_c = eos(usr.rho_c, usr.eos_set, usr.K, usr.gamma)
        elif usr.p_c is not None:
            usr.rho_c = eos_reversed(usr.p_c, usr.eos_set, usr.K, usr.gamma)

        if usr.phi_c is None:
            usr.phi_c = defa.phi_c

        if usr.eps_c is None:
            usr.eps_c = eps(usr.p_c, usr.rho_c, usr.eos_set, usr.gamma)

        print('*************************************************')

    else:
        print('*************************************************')
        print('\t\tCHECKING USER-INPUT\n')

        # eos
        if usr.eos_set is not None:
            if usr.eos_set not in defa.eos_possible:
                print('User input invalid EOS -> Default-Assignment')
                usr.eos_set = defa.eos_set
        else:
            print('User has not defined eos_set-> Default-Assignment')
            usr.eos_set = defa.eos_set
        # K and gamma
        if usr.K is None:
            usr.K = defa.K
        if usr.gamma is None:
            usr.gamma = defa.gamma

        # if rho_c and p_c are define then we use rho_c and p_c as eos bcs otherwise it makes no sense
        if (usr.rho_c is not None and usr.p_c is not None):
            print('User define rho_c and p_c -> conflict\nCode continues with rho_c as defined and p_c according to EoS')
            usr.p_c = eos(usr.rho_c, usr.eos_set, usr.K, usr.gamma)
        elif usr.rho_c is not None:
            usr.p_c = eos(usr.rho_c, usr.eos_set, usr.K, usr.gamma)
        elif usr.p_c is not None:
            usr.rho_c = eos_reversed(usr.p_c, usr.eos_set, usr.K, usr.gamma)
        else:
            print('User has not defined rho_c and p_c -> Default-Assignment')
            usr.rho_c = defa.rho_c
            usr.p_c = defa.p_c

        if usr.phi_c is not None:
            print('Careful how you define Phi_c')
        else:
            usr.phi_c = defa.phi_c

        # eps_c is defined through a function with p_c and rho_c
        if usr.eps_c is not None:
            print('Warning User defined eps_c, this can cause problems with rho_c and p_c')
        else:
            usr.eps_c = eps(usr.p_c, usr.rho_c, usr.eos_set, usr.gamma)

        # check grid
        if usr.grid is not None:
            if not isinstance(usr.grid, int):
                print('User incorrectly defined grid -> Default-Assignment')
                usr.grid = defa.grid
            elif usr.grid > 1e6:
                print('Warning large grid - this can take a while')
            elif usr.grid < 1e3:
                print('Small grid - this can be inaccurate')
        else:
            print('User has not defined grid -> Default-Assignment')
            usr.grid = defa.grid

        # check stepsize
        if usr.stepsize is not None:
            if usr.stepsize > 1e3:
                print('Warning large stepsize - can be inaccurate')
            elif usr.stepsize < 1:
                print('Warning small stepsize - this can take a while')
        else:
            print('User has not defined stepsize -> Default-Assignment')
            usr.stepsize = defa.stepsize

        # check r0
        if usr.r0 is not None:
            if usr.r0 > 1e-5:
                print('Warning large r0 - can be inaccurate')
        else:
            print('User has not defined r0 -> Default-Assignment')
            usr.r0 = defa.r0

        # check r type
        if (usr.r_type is not None or usr.defined_r is not None):
            if usr.r_type is not None:
                if usr.r_type not in defa.r_types_possible:
                    if usr.defined_r is not None:
                        if np.logical_or(isinstance(usr.defined_r, list), isinstance(usr.defined_r, np.ndarray)):
                            usr.r_type = 'unique'
                            print('R-type defined uniquely -> Proceed with CAUTION')
                        else:
                            print('User uniquely defined R-type incorrectly -> Default-Assignment')
                            usr.r_type = defa.r_type
                    else:
                        print('R-type User Input invalid -> Default-Assignment')
                        usr.r_type = defa.r_type
                else:
                    print('User Input for r_type valid')
            else:
                # this means r_type is None but usr.defined_r is something
                if np.logical_or(isinstance(usr.defined_r, list), isinstance(usr.defined_r, np.ndarray)):
                    usr.r_type = 'unique'
                    print('R-type defined uniquely -> Proceed with CAUTION')
                else:
                    print('User uniquely defined R-type incorrectly -> Default-Assignment')
                    usr.r_type = defa.r_type
        else:
            print('User has not defined r_type or defined_r -> Default-Assignment')
            usr.r_type = defa.r_type

        # check r or m cut off
        if usr.cut_off == 'Mass':
            if usr.m_break is not None:
                print('M_break well defined')
            else:
                usr.m_break = defa.m_break
        elif usr.cut_off == 'Radius':
            if usr.r_break is not None:
                print('R_break well defined')
            else:
                usr.r_break = defa.r_break
        else:
            print('User uniquely defined cut_off incorrectly -> Default-Assignment')
            usr.cut_off = defa.cut_off
            usr.m_break = defa.m_break
            usr.r_break = defa.r_break

        # check rk-method
        if usr.rk_method is not None:
            if usr.rk_method not in defa.available_rkmethods:
                print('RK-METHOD defined inccorectly -> Default-Assignment')
                usr.rk_method = defa.rk_method
            else:
                print('RK-METHOD defined correctly')
        else:
            print('RK-method not defined -> Default-Assignment')
            usr.rk_method = defa.rk_method


        print('\n\t\tDONE CHECKING USER-INPUT')
        print('*************************************************')


    return(usr)



def eos(rho, type='poly', K=1.982e-6, gamma=2.75):
    '''
    Equation of State Function

    - Inputs:
        rho := density value
        type := EoS type
        K :=
        gamma :=
    - Outputs:
        p := pressure from EOS
    '''
    # units in cgs
    if type == 'poly':
        # p_c = K * rho_c ** gamma
        return(K * (rho**gamma))

def eos_reversed(p, type='poly', K=1.982e-6, gamma=2.75):
    '''
    Equation of State Function Reversed

    - Inputs:
        p := pressure value
        type := EoS type
        K :=
        gamma :=
    - Outputs:
        rho := density from EOS
    '''
    # units in cgs,
    if type == 'poly':
        # rho_n = (p_n / K) ** (1/gamma)
        return((p/K)**(1/gamma))

def eps(p, rho, type='poly', gamma=2.75):
    '''
    Epsilon Value Function (specific internal energy)

    - Inputs:
        p := pressure value
        rho := density value
        type := EoS type
        gamma :=
    - Outputs:
        eps := specific internal energy value
    '''
    # units in cgs
    if type == 'poly':
        # eps = p / ((gamma-1)*rho)
        return(p / ((gamma-1)*rho))



def dpdr_NEWT(r, rho, p, m, eps=0, c=3e10, G=6.6742e-8):
    '''
    NEWTONIAN CORRECTION for TOV-Equation for Pressure-Differential-Equation

    - Inputs:
        r := position/radius
        rho := density
        p := pressure
        m := mass
        eps := specific internal energy
        c := speed of light
        G := Gravitational constant

    - Outputs:
        return next step for dp/dr TOV equation

    '''
    return(-G * m * rho /(r**2))

def dmdr_NEWT(r, rho, eps=0, c=3e10):
    '''
    NEWTONIAN CORRECTION for TOV-Equation for Mass-Differential-Equation

    - Inputs:
        r := position/radius
        rho := density
        eps := specific internal energy
        c := speed of light

    - Outputs:
        return next step for dm/dr TOV equation

    '''
    return(4 * np.pi * (r**2) * rho)



def dpdr(r, rho, p, m, eps=0, c=3e10, G=6.6742e-8):
    '''
    TOV-Equation for Pressure-Differential-Equation

    - Inputs:
        r := position/radius
        rho := density
        p := pressure
        m := mass
        eps := specific internal energy
        c := speed of light
        G := Gravitational constant

    - Outputs:
        return next step for dp/dr TOV equation

    '''
    #### We ignore the warning because in the last step the pressure goes to zero -> adiabatic equatoin forces error
    warnings.filterwarnings("ignore")
    ####
    return(-G * (rho * (1 + (eps/(c**2))) + (p/(c**2))) * ((m + (4 * np.pi * (r**3) * (p/(c**2)))) / (r * (r - (2 * G * m / (c**2))))))

def dmdr(r, rho, eps=0, c=3e10):
    '''
    TOV-Equation for Mass-Differential-Equation

    - Inputs:
        r := position/radius
        rho := density
        eps := specific internal energy
        c := speed of light

    - Outputs:
        return next step for dm/dr TOV equation

    '''
    return(4 * np.pi * (r**2) * rho * (1 + (eps / (c**2))))



def check_Sim_Done(tov, usr):
    '''
    To check if the Mass of the Star has been reached at the end of the simulation

    - Inputs:
        tov := tov object
        usr := user-input object
    - Returns:
        tov := tov object with check for a completed simulation
    '''

    if (tov.Mstar == 0 or tov.Rstar == 0 or tov.Mstarind == -1):
        tov.Mstar = -1e8
        tov.Rstar = -1e8
        tov.sim_done = False
    return(tov)

def check_MRstar(tov, usr, i):
    '''
    To check if the Mass of the Star has been reached at each step -> defined Mstar

    - Inputs:
        tov := tov object
        usr := user-input object
        i := the index of simulation we are at
    - Returns:
        tov := tov object with check for a completed simulation at i
    '''

    if usr.cut_off == 'Mass':
        if (tov.m[i] >= usr.m_break and tov.Mstar == 0):
            tov.Mstar = tov.m[i]
            tov.Rstar = tov.r[i]
            tov.Mstarind = i
            return(tov)
        else:
            return(tov)
    elif usr.cut_off == 'Radius':
        if (tov.r[i] >= usr.r_break and tov.Rstar == 0):
            tov.Mstar = tov.m[i]
            tov.Rstar = tov.r[i]
            tov.Mstarind = i
            return(tov)
        else:
            return(tov)
    else:
        return(tov)



def radius_Schwarzschild(G, m, c):
    '''
    Determine Schwarzschild radius for specific mass

    - Inputs:
        G := gravitational constant
        m := cummulative mass at specific radius
        c := speed of light

    - Outputs:
        return schwarzschild radius
    '''
    return(2 * G * m / (c**2))



def rk1_incl_epsilon(usr, const, tov):
    '''
    Runge-Kutta 1-Order -- Euler ---- INCLUDING EPSILON

    - Inputs:
        usr := user input Object
        const := constants Object
        tov := TOVmodel Object
    - Outputs:

    '''
    # For RK1
    dpdr_rk = np.zeros(usr.grid+1)
    dmdr_rk = np.zeros(usr.grid+1)
    drhodr_rk = np.zeros(usr.grid+1)
    depsdr_rk = np.zeros(usr.grid+1)
    dphi_dr_rk = np.zeros(usr.grid+1)

    for i in range(0, usr.grid-1):
        dr = tov.r[i+1] - tov.r[i]
        # RK1
        dmdr_rk[i] = dr*dmdr(tov.r[i], tov.rho[i], tov.epsilons[i])
        dpdr_rk[i] = dr*dpdr(tov.r[i], tov.rho[i], tov.p[i], tov.m[i], tov.epsilons[i])
        drhodr_rk[i] = -1*np.abs(tov.rho[i] - eos_reversed(tov.p[i] + dpdr_rk[i], usr.eos_set, usr.K, usr.gamma))

        # now for eps and phi

        # update values
        tov.m[i+1] = tov.m[i] + dmdr_rk[i]
        tov.p[i+1] = tov.p[i] + dpdr_rk[i]
        tov.rho[i+1] = tov.rho[i] + drhodr_rk[i]
        tov.epsilons[i+1] = eps(tov.p[i+1], tov.rho[i+1])

        # check if Mstar is reached
        tov = check_MRstar(tov, usr, i)
        if tov.m[i] >= usr.m_break:
            tov.sim_done = True
            return
        elif math.isnan(tov.m[i+1]):
            # this means it breaks because NAN -> pressure is 0
            tov.Mstar = tov.m[i]
            tov.Mstarind = i
            tov.Rstar = tov.r[i]
            # print('****\n{0}\n****'.format(tov.Mstar))
            # print('****\n{0}\n****'.format(tov.Mstarind))
            tov.Pzero = True
            tov.sim_done = True
            # print('breaking NAN')
            return


    # check if went out to M or R star
    tov = check_Sim_Done(tov, usr)

def rk1_newtonian(usr, const, tov):
    '''
    Runge-Kutta 1-Order -- Euler  ---- NEWTONIAN

    - Inputs:
        usr := user input Object
        const := constants Object
        tov := TOVmodel Object
    - Outputs:

    '''
    # For RK1
    dpdr_rk = np.zeros(usr.grid+1)
    dmdr_rk = np.zeros(usr.grid+1)
    drhodr_rk = np.zeros(usr.grid+1)
    depsdr_rk = np.zeros(usr.grid+1)
    dphi_dr_rk = np.zeros(usr.grid+1)

    for i in range(0, usr.grid-1):
        dr = tov.r[i+1] - tov.r[i]
        # RK1
        dmdr_rk[i] = dr*dmdr_NEWT(tov.r[i], tov.rho[i])
        dpdr_rk[i] = dr*dpdr_NEWT(tov.r[i], tov.rho[i], tov.p[i], tov.m[i])
        drhodr_rk[i] = -1*np.abs(tov.rho[i] - eos_reversed(tov.p[i] + dpdr_rk[i], usr.eos_set, usr.K, usr.gamma))
        # now for eps and phi

        # update values
        tov.m[i+1] = tov.m[i] + dmdr_rk[i]
        tov.p[i+1] = tov.p[i] + dpdr_rk[i]
        tov.rho[i+1] = tov.rho[i] + drhodr_rk[i]

        # check if Mstar is reached
        tov = check_MRstar(tov, usr, i)
        if tov.m[i] >= usr.m_break:
            tov.sim_done = True
            return
        elif math.isnan(tov.m[i+1]):
            # this means it breaks because NAN -> pressure is 0
            tov.Mstar = tov.m[i]
            tov.Mstarind = i
            tov.Rstar = tov.r[i]
            # print('****\n{0}\n****'.format(tov.Mstar))
            # print('****\n{0}\n****'.format(tov.Mstarind))
            tov.Pzero = True
            tov.sim_done = True
            # print('breaking NAN')
            return


    # check if went out to M or R star
    tov = check_Sim_Done(tov, usr)

def rk1(usr, const, tov):
    '''
    Runge-Kutta 1-Order -- Euler

    - Inputs:
        usr := user input Object
        const := constants Object
        tov := TOVmodel Object
    - Outputs:

    '''
    # For RK1
    dpdr_rk = np.zeros(usr.grid+1)
    dmdr_rk = np.zeros(usr.grid+1)
    drhodr_rk = np.zeros(usr.grid+1)
    depsdr_rk = np.zeros(usr.grid+1)
    dphi_dr_rk = np.zeros(usr.grid+1)

    for i in range(0, usr.grid-1):
        dr = tov.r[i+1] - tov.r[i]
        # RK1
        dmdr_rk[i] = dr*dmdr(tov.r[i], tov.rho[i])
        dpdr_rk[i] = dr*dpdr(tov.r[i], tov.rho[i], tov.p[i], tov.m[i])
        drhodr_rk[i] = -1*np.abs(tov.rho[i] - eos_reversed(tov.p[i] + dpdr_rk[i], usr.eos_set, usr.K, usr.gamma))
        # now for eps and phi

        # update values
        tov.m[i+1] = tov.m[i] + dmdr_rk[i]
        tov.p[i+1] = tov.p[i] + dpdr_rk[i]
        tov.rho[i+1] = tov.rho[i] + drhodr_rk[i]

        # check if Mstar is reached
        tov = check_MRstar(tov, usr, i)
        if tov.m[i] >= usr.m_break:
            tov.sim_done = True
            return
        elif math.isnan(tov.m[i+1]):
            # this means it breaks because NAN -> pressure is 0
            tov.Mstar = tov.m[i]
            tov.Mstarind = i
            tov.Rstar = tov.r[i]
            # print('****\n{0}\n****'.format(tov.Mstar))
            # print('****\n{0}\n****'.format(tov.Mstarind))
            tov.Pzero = True
            # print('breaking NAN')
            tov.sim_done = True
            return


    # check if went out to M or R star
    tov = check_Sim_Done(tov, usr)

def rk2(usr, const, tov):
    '''
    Runge-Kutta 2-Order

    - Inputs:
        usr := user input Object
        const := constants Object

    - Outputs:

    '''

    # For RK2
    rk_val = 2
    dpdr_rk = np.zeros((usr.grid+1, rk_val))
    dmdr_rk = np.zeros((usr.grid+1, rk_val))
    drhodr_rk = np.zeros((usr.grid+1, rk_val))
    depsdr_rk = np.zeros((usr.grid+1, rk_val))
    dphi_dr_rk = np.zeros((usr.grid+1, rk_val))

    for i in range(0, usr.grid-1):
        dr = tov.r[i+1] - tov.r[i]
        # RK1
        dmdr_rk[i, 0] = dr*dmdr(tov.r[i], tov.rho[i])
        dpdr_rk[i, 0] = dr*dpdr(tov.r[i], tov.rho[i], tov.p[i], tov.m[i])
        drhodr_rk[i, 0] = -1*np.abs(tov.rho[i] - eos_reversed(tov.p[i] + dpdr_rk[i,0], usr.eos_set, usr.K, usr.gamma))

        # now for eps and phi

        # RK2
        dmdr_rk[i, 1] = dr*dmdr(tov.r[i]+(dr/2), tov.rho[i]+(drhodr_rk[i, 0]/2))
        dpdr_rk[i, 1] = dr*dpdr(tov.r[i]+(dr/2), tov.rho[i]+(drhodr_rk[i, 0]/2), tov.p[i]+(dpdr_rk[i, 0]/2), tov.m[i]+(dmdr_rk[i, 0]/2))
        drhodr_rk[i, 1] = -1*np.abs(tov.rho[i] - eos_reversed(tov.p[i] + dpdr_rk[i, 1]))

        # update values
        tov.m[i+1] = tov.m[i] + dmdr_rk[i, 1]
        tov.p[i+1] = tov.p[i] + dpdr_rk[i, 1]
        tov.rho[i+1] = tov.rho[i] + drhodr_rk[i, 1]


        # check if Mstar is reached
        tov = check_MRstar(tov, usr, i)
        if tov.m[i] >= usr.m_break:
            tov.sim_done = True
            return
        elif math.isnan(tov.m[i+1]):
            # this means it breaks because NAN -> pressure is 0
            tov.Mstar = tov.m[i]
            tov.Mstarind = i
            tov.Rstar = tov.r[i]
            # print('****\n{0}\n****'.format(tov.Mstar))
            # print('****\n{0}\n****'.format(tov.Mstarind))
            tov.Pzero = True
            tov.sim_done = True
            # print('breaking NAN')
            return

    # check if went out to M or R star
    tov = check_Sim_Done(tov, usr)

def rk3(usr, const, tov):
    '''
    Runge-Kutta 3-Order

    - Inputs:
        usr := user input Object
        const := constants Object

    - Outputs:

    '''

    # For RK3
    rk_val = 3
    dpdr_rk = np.zeros((usr.grid+1, rk_val))
    dmdr_rk = np.zeros((usr.grid+1, rk_val))
    drhodr_rk = np.zeros((usr.grid+1, rk_val))
    depsdr_rk = np.zeros((usr.grid+1, rk_val))
    dphi_dr_rk = np.zeros((usr.grid+1, rk_val))

    for i in range(0, usr.grid-1):
        dr = tov.r[i+1] - tov.r[i]
        # RK1
        dmdr_rk[i, 0] = dr*dmdr(tov.r[i], tov.rho[i])
        dpdr_rk[i, 0] = dr*dpdr(tov.r[i], tov.rho[i], tov.p[i], tov.m[i])
        drhodr_rk[i, 0] = -1*np.abs(tov.rho[i] - eos_reversed(tov.p[i] + dpdr_rk[i,0], usr.eos_set, usr.K, usr.gamma))
        # now for eps and phi

        # RK2
        dmdr_rk[i, 1] = dr*dmdr(tov.r[i]+(dr/2), tov.rho[i]+(drhodr_rk[i, 0]/2))
        dpdr_rk[i, 1] = dr*dpdr(tov.r[i]+(dr/2), tov.rho[i]+(drhodr_rk[i, 0]/2), tov.p[i]+(dpdr_rk[i, 0]/2), tov.m[i]+(dmdr_rk[i, 0]/2))
        drhodr_rk[i, 1] = -1*np.abs(tov.rho[i] - eos_reversed(tov.p[i] + dpdr_rk[i, 1]))

        # RK3
        dmdr_rk[i, 2] = dr*dmdr(tov.r[i]+(dr/2), tov.rho[i]+(drhodr_rk[i, 1]/2))
        dpdr_rk[i, 2] = dr*dpdr(tov.r[i]+(dr/2), tov.rho[i]+(drhodr_rk[i, 1]/2), tov.p[i]+(dpdr_rk[i, 1]/2), tov.m[i]+(dmdr_rk[i, 1]/2))
        drhodr_rk[i, 2] = -1*np.abs(tov.rho[i] - eos_reversed(tov.p[i] + dpdr_rk[i, 2]))

        # update values
        tov.m[i+1] = tov.m[i] + ((dmdr_rk[i, 0] + 4*dmdr_rk[i, 1] + dmdr_rk[i, 2])/6)
        tov.p[i+1] = tov.p[i] + ((dpdr_rk[i, 0] + 4*dpdr_rk[i, 1] + dpdr_rk[i, 2])/6)
        tov.rho[i+1] = tov.rho[i] + ((drhodr_rk[i, 0] + 4*drhodr_rk[i, 1] + drhodr_rk[i, 2])/6)

        # check if Mstar is reached
        tov = check_MRstar(tov, usr, i)
        if tov.m[i] >= usr.m_break:
            tov.sim_done = True
            return
        elif math.isnan(tov.m[i+1]):
            # this means it breaks because NAN -> pressure is 0
            tov.Mstar = tov.m[i]
            tov.Mstarind = i
            tov.Rstar = tov.r[i]
            # print('****\n{0}\n****'.format(tov.Mstar))
            # print('****\n{0}\n****'.format(tov.Mstarind))
            tov.Pzero = True
            tov.sim_done = True
            # print('breaking NAN')
            return

    # check if went out to M or R star
    tov = check_Sim_Done(tov, usr)

def rk4(usr, const, tov):
    '''
    Runge-Kutta 4-Order

    - Inputs:
        usr := user input Object
        const := constants Object

    - Outputs:

    '''

    # For RK4
    rk_val = 4
    dpdr_rk = np.zeros((usr.grid+1, rk_val))
    dmdr_rk = np.zeros((usr.grid+1, rk_val))
    drhodr_rk = np.zeros((usr.grid+1, rk_val))
    depsdr_rk = np.zeros((usr.grid+1, rk_val))
    dphi_dr_rk = np.zeros((usr.grid+1, rk_val))

    for i in range(0, usr.grid-1):
        dr = tov.r[i+1] - tov.r[i]
        # RK1
        dmdr_rk[i, 0] = dr*dmdr(tov.r[i], tov.rho[i])
        dpdr_rk[i, 0] = dr*dpdr(tov.r[i], tov.rho[i], tov.p[i], tov.m[i])
        drhodr_rk[i, 0] = -1*np.abs(tov.rho[i] - eos_reversed(tov.p[i] + dpdr_rk[i,0], usr.eos_set, usr.K, usr.gamma))
        # now for eps and phi

        # RK2
        dmdr_rk[i, 1] = dr*dmdr(tov.r[i]+(dr/2), tov.rho[i]+(drhodr_rk[i, 0]/2))
        dpdr_rk[i, 1] = dr*dpdr(tov.r[i]+(dr/2), tov.rho[i]+(drhodr_rk[i, 0]/2), tov.p[i]+(dpdr_rk[i, 0]/2), tov.m[i]+(dmdr_rk[i, 0]/2))
        drhodr_rk[i, 1] = -1*np.abs(tov.rho[i] - eos_reversed(tov.p[i] + dpdr_rk[i, 1]))

        # RK3
        dmdr_rk[i, 2] = dr*dmdr(tov.r[i]+(dr/2), tov.rho[i]+(drhodr_rk[i, 1]/2))
        dpdr_rk[i, 2] = dr*dpdr(tov.r[i]+(dr/2), tov.rho[i]+(drhodr_rk[i, 1]/2), tov.p[i]+(dpdr_rk[i, 1]/2), tov.m[i]+(dmdr_rk[i, 1]/2))
        drhodr_rk[i, 2] = -1*np.abs(tov.rho[i] - eos_reversed(tov.p[i] + dpdr_rk[i, 2]))

        # RK4
        dmdr_rk[i, 3] = dr*dmdr(tov.r[i]+dr, tov.rho[i]+drhodr_rk[i, 2])
        dpdr_rk[i, 3] = dr*dpdr(tov.r[i]+dr, tov.rho[i]+drhodr_rk[i, 2], tov.p[i]+dpdr_rk[i, 2], tov.m[i]+dmdr_rk[i, 2])
        drhodr_rk[i, 3] = -1*np.abs(tov.rho[i] - eos_reversed(tov.p[i] + dpdr_rk[i, 3]))

        # update values
        tov.m[i+1] = tov.m[i] + (((dmdr_rk[i, 0] + dmdr_rk[i, 3])/6) + ((dmdr_rk[i, 1] + dmdr_rk[i, 2])/3))
        tov.p[i+1] = tov.p[i] + (((dpdr_rk[i, 0] + dpdr_rk[i, 3])/6) + ((dpdr_rk[i, 1] + dpdr_rk[i, 2])/3))
        tov.rho[i+1] = tov.rho[i] + (((drhodr_rk[i, 0] + drhodr_rk[i, 3])/6) + ((drhodr_rk[i, 1] + drhodr_rk[i, 2])/3))

        # check if Mstar is reached
        tov = check_MRstar(tov, usr, i)
        if tov.m[i] >= usr.m_break:
            tov.sim_done = True
            return
        elif math.isnan(tov.m[i+1]):
            # this means it breaks because NAN -> pressure is 0
            tov.Mstar = tov.m[i]
            tov.Mstarind = i
            tov.Rstar = tov.r[i]
            # print('****\n{0}\n****'.format(tov.Mstar))
            # print('****\n{0}\n****'.format(tov.Mstarind))
            tov.Pzero = True
            tov.sim_done = True
            # print('breaking NAN')
            return

    # check if went out to M or R star
    tov = check_Sim_Done(tov, usr)


def save_res(usr1, const, tov1):
    '''
    To save results from RK-run

    - Inputs:
        usr1 := user input Object
        const := constants Object
        tov1 := TOVmodel Object
    - Outputs:
        save pickle file with results
    '''
    fullfilename = usr1.save_path + usr1.save_name + '.pkl'
    if not os.path.exists(usr1.save_path):
        print('Save-Direcoty does not exist -> creating directory to save')
        os.makedirs(usr1.save_path)
    else:
        if usr1.save_name + '.pkl' in [x for x in os.listdir(usr1.save_path)]:
            print('***** WARNING: File already exists in directory *****')
            if usr1.save_over:
                print('Saving File {0} -> old file removed'.format(usr1.save_name + '.pkl'))
            else:
                print('User decided not to overwrite files -> Not Saving : CHANGE FILE NAME')
                return
        else:
            print('File with this file name does not exist yet -> saving')

    # create dictionary
    datasave = {}
    datasave['usr1'] = usr1.__dict__
    datasave['usr1'].pop('const')
    datasave['const'] = const.__dict__
    datasave['tov1'] = tov1.__dict__
    datasave['tov1'].pop('usr')
    datasave['FinalResults'] = {'StarRadius_km': tov1.Rstar * 1e-5,
                                'StarMass_Msun': tov1.Mstar / const.M_sun,
                                'SimulationSteps': tov1.Mstarind}

    try:
        # create the dictionary
        f = open(fullfilename,"wb")
        # write the python object (dict) to pickle file
        pickle.dump(datasave,f)
        # close file
        f.close()

        print('Succesfully saved data into\n{0}'.format(fullfilename))
    except:
        print('Unable to save data into\n{0}'.format(fullfilename))
    return

def graph_res(usr1, const, tov1):
    '''
    To graph results from RK-run

    - Inputs:
        usr := user input Object
        const := constants Object
        tov1 := TOVmodel Object
    - Outputs:
        displays plots
    '''
    try:
        gs = gridspec.GridSpec(2, 2)

        fig = plt.figure()
        ax1 = fig.add_subplot(gs[0, 0]) # row 0, col 0
        ax2 = fig.add_subplot(gs[0, 1]) # row 0, col 1
        ax3 = fig.add_subplot(gs[1, :]) # row 1, span all columns

        ax1.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.m[:tov1.Mstarind], const.M_sun))
        ax2.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), tov1.p[:tov1.Mstarind])
        ax3.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.rho[:tov1.Mstarind], const.rho_nuc))
        ax1.set_xscale('log')
        ax1.set_xlim(1e-1, 2e1)
        ax2.set_xlim(1e-1, 2e1)
        ax3.set_xlim(1e-1, 2e1)
        ax2.set_xscale('log')
        ax3.set_xscale('log')
        # ax3.legend(title='M_star', loc='center left', bbox_to_anchor=(1, 0.5))
        ax1.set_title('Mass of Object\nas function of Radius')
        ax2.set_title('Pressure of Object\nas function of Radius')
        ax3.set_title('Density of Object\nas function of Radius')
        fig.tight_layout()
        plt.show()
    except:
        print('** Unable to Plot results **')

    return

def run_results_output(usr, const, tov):
    '''
    To print (and coordinate saving/plotting) the results of the RK-run in terminal

    - Inputs:
        usr := user input Object
        const := constants Object
        tov := TOVmodel Object
    - Outputs:
        print the results in terminal
    '''
    if tov.sim_done:
        print('\n\n*************************************************')
        print('\t SIMULATION FINISHED')
        print('*************************************************')
        print('\n -------- Initial Inputs --------')
        print('EOS                       :\t {0}'.format(usr.eos_set))
        print('Adiabatic Coefficient (K) :\t {0}'.format(usr.K))
        print('Adiabtic Index (Gamma)    :\t {0}'.format(usr.gamma))
        print('Central-Density (rho_c)   :\t {0}'.format(usr.rho_c))
        print('Grid-size                 :\t {0}'.format(usr.grid))
        print('Step-size                 :\t {0}'.format(usr.stepsize))
        print('Central-Radius (r0)       :\t {0}'.format(usr.r0))
        print('Runge-Kutta Method        :\t {0}'.format(usr.rk_method))
        print('\n -------- Run Results --------')
        print('Star Radius [km]           :\t {0}'.format(round(tov.Rstar *1e-5, 3)))
        print('Star Mass [M_sun]          :\t {0}'.format(round(tov.Mstar / const.M_sun, 3)))
        print('Simulation Steps           :\t {0}'.format(tov.Mstarind))

        if usr.show_graph_res:
            print('\n -------- Showing Graphic Results --------')
            graph_res(usr, const, tov)
        if usr.save_results:
            print('\n -------- Saving Raw Results --------')
            save_res(usr, const, tov)
            print('\n Quitting tov-solver')
            return
        else:
            print('\n Quitting tov-solver')
            return

    else:
        print('\n\n*************************************************')
        print('\t SIMULATION UNFINISHED')
        print('- for the initial input values, the full star was not simulated')
        print('- this means the Star Radius/Mass was not fully determined and Pressure has not gone to zero')
        print('- A place to start to correct for this: Increase gridsize or decrease stepsize!')
        print('*************************************************')
        print('\n Quitting tov-solver')
        return

    return
