'''
name: analysisfunctions
date: 27.01.2022
author: @mauritzwicker
repo: ../

Purpose: To hold tov-solver analysis functions

'''

# Imports
from results_loaded import ResultsLoaded

import numpy as np
import math
import warnings
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pickle
import time
import psutil
import datetime
import os
import sys

# adding Folder_2/subfolder to the system path
sys.path.insert(0, '../')
from constants import Constants
from default_input import DefaultInput
from user_input import UserInput
from tovmodel import TOVmodel
import functions as fcts


def analyseDataSelf(filenames = ['../results/tov-solver_sim1.pkl']):
    '''
    Function to work with the data. Idea is to load data so that a user can do with it as the want

    - Inputs:
        filenames = list of the files a user wants to load for this
    '''

    loaded_objs = []
    for filename in filenames:
        with (open(filename, "rb")) as openfile:
            loaded_objs.append(ResultsLoaded(pickle.load(openfile)))

    # Now a user has a list called loaded_objs with the ResultsLoaded objects
    # ...
    # your code here
    # ...

    return

def print_results(resultsfiles):
    '''
    To simply print the star Mass and Radius and Simulation-Steps.

    - Inputs:
        resultsfiles := list of ResultsLoaded Objects
    '''
    for rf in resultsfiles:
        print('\n -------- Run {0} Results --------'.format(rf.name))
        print('Star Radius [km]           :\t {0}'.format(round(rf.finRes['StarRadius_km'], 3)))
        print('Star Mass [M_sun]          :\t {0}'.format(round(rf.finRes['StarMass_Msun'], 3)))
        print('Simulation Steps           :\t {0}'.format(rf.finRes['SimulationSteps']))

    return

def plot_MProfiles(resultsfiles):
    '''
    To plot the Mass profile

    - Inputs:
        resultsfiles := list of ResultsLoaded Objects
    '''
    for rf in resultsfiles:
        plt.plot(rf.const['R_sun_km'] * np.divide(rf.tov1['r'][:rf.tov1['Mstarind']], rf.const['R_sun']), np.divide(rf.tov1['m'][:rf.tov1['Mstarind']], rf.const['M_sun']), label='M-{0} R-{1}'.format(round(rf.finRes['StarMass_Msun'], 3), round(rf.finRes['StarRadius_km'], 3)))
    plt.xlabel('r  [km]')
    plt.xscale('log')
    plt.xlim(1e-1, 2e1)
    plt.legend(title='Sim Mass[M_sun] & R[km]')
    plt.ylabel('Mass  [' r'$M_{\odot}$' ']')
    plt.show()
    return

def plot_PProfiles(resultsfiles):
    '''
    To plot the Pressure profile

    - Inputs:
        resultsfiles := list of ResultsLoaded Objects
    '''

    for rf in resultsfiles:
        plt.plot(rf.const['R_sun_km'] * np.divide(rf.tov1['r'][:rf.tov1['Mstarind']], rf.const['R_sun']), rf.tov1['p'][:rf.tov1['Mstarind']], label='M-{0} R-{1}'.format(round(rf.finRes['StarMass_Msun'], 3), round(rf.finRes['StarRadius_km'], 3)))
    plt.xlabel('r  [km]')
    plt.xscale('log')
    plt.xlim(1e-1, 2e1)
    plt.legend(title='Sim Mass[M_sun] & R[km]')
    plt.ylabel('Pressure  [' r'$dyn \cdot cm^{-2}$' ']')
    plt.show()
    return

def plot_RhoProfiles(resultsfiles):
    '''
    To plot the Density profile

    - Inputs:
        resultsfiles := list of ResultsLoaded Objects
    '''

    for rf in resultsfiles:
        plt.plot(rf.const['R_sun_km'] * np.divide(rf.tov1['r'][:rf.tov1['Mstarind']], rf.const['R_sun']), np.divide(rf.tov1['rho'][:rf.tov1['Mstarind']], rf.const['rho_nuc']), label='M-{0} R-{1}'.format(round(rf.finRes['StarMass_Msun'], 3), round(rf.finRes['StarRadius_km'], 3)))
    plt.xlabel('r  [km]')
    plt.xscale('log')
    plt.xlim(1e-1, 2e1)
    plt.legend(title='Sim Mass[M_sun] & R[km]')
    plt.ylabel('Density  [' r'$\rho_{nuc}$' ']')
    plt.show()
    return

def plot_MPRhoProfiles(resultsfiles):
    '''
    To plot the Mass, Pressure, Density profiles for a single

    - Inputs:
        resultsfiles := list of ResultsLoaded Objects
    '''
    gs = gridspec.GridSpec(2, 2)
    fig = plt.figure()
    ax1 = fig.add_subplot(gs[0, 0]) # row 0, col 0
    ax2 = fig.add_subplot(gs[0, 1]) # row 0, col 1
    ax3 = fig.add_subplot(gs[1, :]) # row 1, span all columns

    for rf in resultsfiles:
        ax1.plot(rf.const['R_sun_km'] * np.divide(rf.tov1['r'][:rf.tov1['Mstarind']], rf.const['R_sun']), np.divide(rf.tov1['m'][:rf.tov1['Mstarind']], rf.const['M_sun']))
        ax2.plot(rf.const['R_sun_km'] * np.divide(rf.tov1['r'][:rf.tov1['Mstarind']], rf.const['R_sun']), rf.tov1['p'][:rf.tov1['Mstarind']])
        ax3.plot(rf.const['R_sun_km'] * np.divide(rf.tov1['r'][:rf.tov1['Mstarind']], rf.const['R_sun']), np.divide(rf.tov1['rho'][:rf.tov1['Mstarind']], rf.const['rho_nuc']), label='M-{0} R-{1}'.format(round(rf.finRes['StarMass_Msun'], 3), round(rf.finRes['StarRadius_km'], 3)))
    ax1.set_xscale('log')
    ax1.set_xlim(1e-1, 2e1)
    ax2.set_xlim(1e-1, 2e1)
    ax3.set_xlim(1e-1, 2e1)
    ax2.set_xscale('log')
    ax3.set_xscale('log')
    ax3.legend(title='Sim Mass[M_sun] & R[km]', loc='center left', bbox_to_anchor=(1, 0.5))
    ax1.set_title('Mass of Object\nas function of Radius')
    ax2.set_title('Pressure of Object\nas function of Radius')
    ax3.set_title('Density of Object\nas function of Radius')
    fig.tight_layout()
    plt.show()
    return

def plot_MRcentralrho(resultsfiles):
    '''
    To plot the Mass and Radius for different central densities

    - Inputs:
        resultsfiles := list of ResultsLoaded Objects
    '''

    # Mass and Radius for different central densities
    rho_cvals = []
    mstar_vals = []
    rstar_vals = []
    for rf in resultsfiles:
        rho_cvals.append(rf.usr1['rho_c'])
        mstar_vals.append(rf.finRes['StarMass_Msun'])
        rstar_vals.append(rf.finRes['StarRadius_km'])

    fig, ax = plt.subplots(1,2, sharex=True)
    ax[0].scatter(rho_cvals, mstar_vals, color='darkblue', marker='.', s=30)
    ax[0].set_xlabel('Central-Density  [' r'$\rho_{nuc}$' ']')
    ax[0].set_ylabel('Star-Mass  [' r'$M_{\odot}$' ']')
    # R(rho_c)
    ax[1].scatter(rho_cvals, rstar_vals, color='darkblue', marker='.', s=30)
    ax[1].set_xlabel('Central-Density  [' r'$\rho_{nuc}$' ']')
    ax[1].set_ylabel('Star-Radius  [km]')
    plt.show()

def plot_MRRelation(resultsfiles):
    '''
    To plot the Mass-Radius-Relation

    - Inputs:
        resultsfiles := list of ResultsLoaded Objects
    '''

    # Mass and Radius for different central densities
    rho_cvals = []
    mstar_vals = []
    rstar_vals = []
    for rf in resultsfiles:
        rho_cvals.append(rf.usr1['rho_c'])
        mstar_vals.append(rf.finRes['StarMass_Msun'])
        rstar_vals.append(rf.finRes['StarRadius_km'])

    plt.scatter(mstar_vals, rstar_vals, color='darkblue')
    plt.xlabel('Star-Mass  [' r'$M_{\odot}$' ']')
    plt.xlabel('Star-Radius  [km]')
    plt.show()

def load_pickle(fp, fns):
    '''
    To load the pickle objects for each of the wanted files

    - Inputs:
        fp := filepath
        fns := filenames
    - Outputs:
        loaded_objs := list of the pickle files opened as ResultsLoaded objects
    '''
    loaded_objs = []
    for fn in fns:
        if fn[-3:] != 'pkl':
            print('FILE IS NOT PICKLE FILES -> Skipping')
        else:
            with (open(fp + fn, "rb")) as openfile:
                loaded_objs.append(ResultsLoaded(pickle.load(openfile)))

    if len(loaded_objs) != 0:
        return(loaded_objs)
    else:
        return(None)
