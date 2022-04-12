'''
project: TOV-Solver
name: results_loaded
date: 27.01.2022
author: @mauritzwicker
repo: /tov-solver

Purpose: To hold the loaded results object.

'''

class ResultsLoaded:

    def __init__(self, obj):
        # the loaded pickle object
        self.loaded_obj = obj

        self.name = self.loaded_obj['usr1']['save_name']
        self.const = self.loaded_obj['const']
        self.usr1 = self.loaded_obj['usr1']
        self.tov1 = self.loaded_obj['tov1']
        self.finRes = self.loaded_obj['FinalResults']

