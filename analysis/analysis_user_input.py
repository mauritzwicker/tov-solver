'''
project: TOV-Solver
name: analysis_user_input
date: 27.01.2022
author: @mauritzwicker
repo: /tov-solver

Purpose: To hold USER inputs needed for ANALYSIS of tov solver, in form of a AnalysisUserInput Class.

'''

class AnalysisUserInput:
    # general format is if = None -> eather defined through function or default is taken

    def __init__(self):
        # path to the files to analysis (should be in same directory)
        self.filepathAna = '../results/'
        # list of the filenames to use for analysis
        self.filenamesAna = ['tov-solver_sim1.pkl']


        # WHICH ANALYSIS TO DO:

        # whether to print the results of the Simulations
        self.do_print_results = True

        # whether to plot the mass profiles of the Simulations
        self.do_plot_MProfiles = False
        # whether to plot the pressure profiles of the Simulations
        self.do_plot_PProfiles = False
        # whether to plot the density profiles of the Simulations
        self.do_plot_RhoProfiles = False
        # whether to plot the mass, pressure, and density profiles of the Simulations in subplots
        self.do_plot_MPRhoProfiles = True

        # whether to plot Star-Mass and Star-Radius as functions of the central density of the Simulations
        self.do_plot_MRcentralrho = False
        # whether to plot Star-Mass - Star-Radius - Relation
        self.do_plot_MRRelation = False

        # whether to run seld defined analysis function
        self.do_analyseDataSelf = False
