'''
project: TOV-Solver
name: run_analysis
date: 27.01.2022
author: @mauritzwicker
repo: /tov-solver

Purpose: To run analysis of pkl file data

'''

# Imports
from analysis_user_input import AnalysisUserInput

import analysisfunctions as anafcts

import numpy as np
import math
import os
import matplotlib.pyplot as plt
import scipy.constants as cn
import time
import psutil
import os
import datetime
import matplotlib.gridspec as gridspec
import matplotlib.pylab as pl


def main():
    '''
    main function to run analysis

    - Inputs:
        NONE
    - Returns:
        NONE
    '''

    # Load Analysis-user_input object
    useran = AnalysisUserInput()

    # open the files
    resultsfiles = anafcts.load_pickle(useran.filepathAna, useran.filenamesAna)

    if resultsfiles is not None:
        if useran.do_print_results:
            print('\nPrinting Results')
            anafcts.print_results(resultsfiles)
        if useran.do_plot_MProfiles:
            print('\nPlotting MProfiles')
            anafcts.plot_MProfiles(resultsfiles)
        if useran.do_plot_PProfiles:
            print('\nPlotting PProfiles')
            anafcts.plot_PProfiles(resultsfiles)
        if useran.do_plot_RhoProfiles:
            print('\nPlotting RhoProfil')
            anafcts.plot_RhoProfiles(resultsfiles)
        if useran.do_plot_MPRhoProfiles:
            print('\nPlotting MPRhoProf')
            anafcts.plot_MPRhoProfiles(resultsfiles)
        if useran.do_plot_MRcentralrho:
            print('\nPlotting MRcentral')
            anafcts.plot_MRcentralrho(resultsfiles)
        if useran.do_plot_MRRelation:
            print('\nPlotting MRRelatio')
            anafcts.plot_MRRelation(resultsfiles)
        if useran.do_analyseDataSelf:
            print('\nPlotting analyseDataSel')
            anafcts.analyseDataSelf(resultsfiles)
    else:
        print('No Files Opened -> QUITTING')
        quit()
    return


if __name__ == '__main__':
    os.system('clear')
    t_start = time.perf_counter()
    process = psutil.Process(os.getpid())
    ########

    main()

    ########
    #Done
    t_fin = time.perf_counter()
    print('\n \n \n********* Process-{0} ({1}) over ************'.format(process.pid, process.name()))
    print('Runtime: {0} seconds'.format(round(t_fin - t_start), 4))
    p_mem = process.memory_info()
    print('Memory used: {0} bytes ({1} GB) '.format(p_mem.rss, round(p_mem.rss/(1e9), 3)))
    ########################################




