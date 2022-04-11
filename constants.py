'''
project: TOV-Solver
name: constants
date: 27.01.2022
author: @mauritzwicker
repo: /tov-solver

Purpose: To hold constants needed for tov solver, in form of a Constants Class.

'''

# Imports
import numpy as np
import astropy.constants as apc

class Constants:

    def __init__(self, ):
        self.obj_description = 'Object to hold the constants (in cgs) we need to solve the TOV-equation'

        ##########
        # in cgs
        ##########

        # Gravitational constant
        self.G = apc.G.cgs.value
        self.G_unit = apc.G.cgs.unit

        # Earth Mass
        self.M_earth = apc.M_earth.cgs.value
        self.M_earth_unit = apc.M_earth.cgs.unit
        # Solar Mass
        self.M_sun = apc.M_sun.cgs.value
        self.M_sun_unit = apc.M_sun.cgs.unit

        # Earth Equatorial Radius
        self.R_earth = apc.R_earth.cgs.value
        self.R_earth_unit = apc.R_earth.cgs.unit
        # Solar Radius
        self.R_sun = apc.R_sun.cgs.value
        self.R_sun_unit = apc.R_sun.cgs.unit
        self.R_sun_km = 695508  # km

        # Astronomical Units
        self.au = apc.au.cgs.value
        self.au_unit = apc.au.cgs.unit

        # Speed of Light in vacuum
        self.c = apc.c.cgs.value
        self.c_unit = apc.c.cgs.unit

        # Electron charge
        self.e_charge = apc.e.value
        self.e_chage_unit = apc.e.unit

        # Planck Constant
        self.h = apc.h.cgs.value
        self.h_unit = apc.h.cgs.unit

        # Boltzmann constant
        self.k_b = apc.k_B.cgs.value
        self.k_b_unit = apc.k_B.cgs.unit

        # Stefan-Boltzmann Constant
        self.sigma_sb = apc.sigma_sb.cgs.value
        self.sigma_sbunit = apc.sigma_sb.cgs.unit

        # Parsec in cm
        self.pc = apc.pc.cgs.value
        self.pc_unit = apc.pc.cgs.unit

        # Electron mass in cm
        self.m_e = apc.m_e.cgs.value
        self.m_e_unit = apc.m_e.cgs.unit

        # Neutron mass in cm
        self.m_n = apc.m_n.cgs.value
        self.m_n_unit = apc.m_n.cgs.unit

        # Proton mass in cm
        self.m_p = apc.m_p.cgs.value
        self.m_p_unit = apc.m_p.cgs.unit

        # nuclear density
        self.rho_nuc = 2.7*1e14 # g/cm3
