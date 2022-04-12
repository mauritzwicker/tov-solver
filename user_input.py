'''
project: TOV-Solver
name: user_input
date: 27.01.2022
author: @mauritzwicker
repo: /tov-solver

Purpose: To hold USER inputs needed for tov solver, in form of a UserInput Class.

'''

class UserInput:
    # general format is if = None -> eather defined through function or default is taken

    def __init__(self, const_obj):
        self.const = const_obj
        self.obj_description = 'Object to hold the user defined inputs to solve the TOV-Equation'

        # Whether to use default values or to use user_defined
        self.use_default = False

        # For EoS
        #  eos_set := the selected equation of state
        self.eos_set = 'poly'
        # K := adiabatic constant
        self.K = 1.982e-6
        # gamma := adiabatic coefficient
        self.gamma = 2.75

        # rho_c := central_density
        # self.rho_c = 5.0e14 # g cm-3
        self.rho_c = 2 * self.const.rho_nuc
        # p_c := central pressure
        self.p_c = None
        # eps_c := central specific internal energy
        self.eps_c = None
        # phi_c := central metric potential
        self.phi_c = None

        # m_c := central mass (should be zero)
        self.m_c = 0

        # r0 := the smalles radius to start at (r->0)
        self.r0 = 1e-8

        # m_break := the Mass at which we break off
        self.m_break = 100 * self.const.M_sun # g

        # r_break := radius at which to break
        self.r_break = 1 * self.const.R_sun

        # grid := the gridsize for the model
        self.grid = int(4e6)
        # stepsize := the stepsize in the grid
        self.stepsize = 100

        # r_type := the way we want to define our stepwise iteration
        self.r_type = 'lin'
        self.defined_r = ['lin']
        # possibility to implement logarithmic or other steps

        # define cut off
        self.cut_off = 'Mass'
        self.defined_coutoff = ['Mass', 'Radius']

        # which rk_method to use
        self.rk_method = 'rk4'

        # Whether to check user input of not
        self.check_inputs = True

        # Whether to print some basic graphs for result
        self.show_graph_res = False

        # Whether to save data
        self.save_results = True
        # Where to save file
        self.save_path = './results/'
        # What name to save file under
        self.save_name = 'tov-solver_sim2'
        # Whether to overwrite saved files
        self.save_over = False
