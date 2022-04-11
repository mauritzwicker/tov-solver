'''
project: TOV-Solver
name: default_input
date: 27.01.2022
author: @mauritzwicker
repo: /tov-solver

Purpose: To hold default inputs needed for tov solver, in form of a DefaultInput Class.

'''

# Imports
import functions as fcts

class DefaultInput:
    # general format is if = None -> eather defined through function or default is taken

    def __init__(self, const_obj):
        self.const = const_obj
        self.obj_description = 'Object to hold the default defined inputs to solve the TOV-Equation'

        ####################
        # Define System-Run-Format
        # - this is so that in case run formats want to be considered, like comparing multiple EoS at once, it could be implemented
        self.run_format = 'simple'
        self.run_fomats = ['simple']
        ####################

        # For EoS
        # eos_possible := the possible eos
        self.eos_possible = ['poly']
        # eos_set := the selected equation of state
        self.eos_set = 'poly'
        # K := Adiabatic Constant
        self.K = 1.982e-6
        # gamma := Adiabatic Coefficient
        self.gamma = 2.75

        # rho_c := Central Density
        self.rho_c = 5.0e14 # g cm-3
        # p_c := Central Pressure
        self.p_c = fcts.eos(self.rho_c, self.eos_set, self.K, self.gamma)
        # eps_c := Central Specific Internal Energy
        self.eps_c = fcts.eps(self.p_c, self.rho_c, self.eos_set, self.gamma)
        # phi_c := Central Metric Potential
        self.phi_c = 0

        # m_c := Central Mass (should always be set to zero because it is defined in our functions)
        self.m_c = 0

        # m_break := the Mass at which we break off the simulation
        self.m_break = 100 * self.const.M_sun # g
        # r_break := radius at which to break off the simulation
        self.r_break = 1 * self.const.R_sun
        # **** M_break and R_break are to limit the simulation from running infinitely
        # - If this mass is reached, the pressure is not zero yet.
        # - If pressure is zero, this mass is nto reached

        # grid := the gridsize for the model (so how many datapoints)
        self.grid = int(1e6)
        # stepsize := the stepsize in the grid (so how exact)
        self.stepsize = 100
        # **** If the Mass and Radius of Star have been reached (pressure to zero) not the whole grid is evaluated

        # r0 := the smalles radius to start at (r->0)
        self.r0 = 1e-8

        # r_type := the way we want to define our stepwise iteration
        self.r_type = 'lin'
        # possible r_types
        self.r_types_possible = ['lin']

        # define cut off
        self.cut_off = 'Mass'
        self.defined_coutoff = ['Mass', 'Radius']

        # which rk_method to use
        self.rk_method = 'rk4'
        self.available_rkmethods = ['rk1', 'rk2', 'rk3', 'rk4']

        # Whether to print some basic graphs for result
        self.show_graph_res = False

        # Whether to save data
        self.save_results = True
        self.save_path = './results/'
        self.save_name = 'tov-solver_sim1'
        self.save_over = False
