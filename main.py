'''
project: TOV-Solver
name: main
date: 27.01.2022
author: @mauritzwicker
repo: /tov-solver

Purpose: Main program to run tov-solver.

'''

# Imports
from constants import Constants
from default_input import DefaultInput
from user_input import UserInput
from tovmodel import TOVmodel

import functions as fcts

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
    main function to run tov-solver

    - Inputs:
        NONE
    - Returns:
        NONE
    '''

    # initialize constants objects
    const = Constants()

    # initialize default inputs object
    defa = DefaultInput(const)

    # create user object
    usr_unchecked = UserInput(const)

    print()

    # check user object or assign as default
    if usr_unchecked.use_default:
        usr1 = defa
        print('*************************************************')
        print('\t Using Default Values for Model')
        print('*************************************************')
    else:
        usr1 = fcts.check_userinput(const, defa, usr_unchecked)

    # create the tov model
    tov1 = TOVmodel(usr1, const)

    # run desired RK-method
    if usr1.rk_method == 'rk1':
        fcts.rk1(usr1, const, tov1)
    elif usr1.rk_method == 'rk2':
        fcts.rk2(usr1, const, tov1)
    elif usr1.rk_method == 'rk3':
        fcts.rk3(usr1, const, tov1)
    elif usr1.rk_method == 'rk4':
        fcts.rk4(usr1, const, tov1)
    else:
        print('Model defined incorrectly -> quitting')
        quit()

    # Simulation Done
    fcts.run_results_output(usr1, const, tov1)


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
