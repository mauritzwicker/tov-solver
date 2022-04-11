'''
project: TOV-Solver
name: tovmodel
date: 27.01.2022
author: @mauritzwicker
repo: /tov-solver

Purpose: To hold TOVmodel object, which is the simulation model.

'''

# Imports
from functions import *
import numpy as np

class TOVmodel:

    def __init__(self, usr, const):
        self.usr = usr
        self.const = const

        self.init_variables()

        # determine Schwarzschild Radius
        self.r_ss = radius_Schwarzschild(const.G, usr.m_break, const.c)

        # initiate Mstar variable
        self.Mstar = 0
        # initiate Rstar variable
        self.Rstar = 0
        # initiate Mstar index
        self.Mstarind = -1

        # initiate pressure warning
        self.Pzero = False

    def init_variables(self):
        '''
        To initiate variables from User input
        '''

        # R (distance/radius)
        if self.usr.r_type == 'lin':
            self.r = np.linspace(self.usr.r0, (self.usr.grid*self.usr.stepsize)-1, int(self.usr.grid))
        elif self.usr.r_type == 'log':
            self.r = np.logspace(np.log10(self.usr.r0), np.log10((self.usr.grid*self.usr.stepsize)-1), self.usr.grid)
        elif self.usr.r_type == 'unique':
            self.r = self.usr.defined_r

        # Pressure
        self.p = np.zeros(self.usr.grid)
        self.p[0] = self.usr.p_c

        # Density
        self.rho = np.zeros(self.usr.grid)
        self.rho[0] = self.usr.rho_c

        # Mass
        self.m = np.zeros(self.usr.grid)
        self.m[0] = self.usr.m_c

        # Specific Enthalpy Value
        self.epsilons = np.zeros(self.usr.grid)
        self.epsilons[0] = self.usr.eps_c

        # Gravitational Potential
        self.phi = np.zeros(self.usr.grid)
        self.phi[0] = self.usr.phi_c




        ### LOOK TO COMBINE THIS INTO ONE LARGE ARRAY -> not as many objects
        # And how to determine starting values!!

