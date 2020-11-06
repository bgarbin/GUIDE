# -*- coding: utf-8 -*-

import numpy as np
#import cmath as cm

# Main parameters for window
#     'record_every': number of time_steps one between two consecutive record events

window_params = {'kernel': 'RK4','nstep_update_plot': 100, 'step_size': 0.01, 'array_size': 10000, 'streaming': True, 'record_state':False, 'nstep_record':1, 'window_size':(1200,1000), 'invert_order_obs_var': True}#,'theme':'dark'}


# Definition of the plot configuration
def load_docks():
    
    ''' Returns a dict to be used for plots declaration. Here, we use pyqtgraph docks. Each plot has a dictionnary as "value" with keys: "type" (accepted values: 'plot' and 'image'), "zoomOf" (key name of another dock), "position" (accepted values: 'bottom', 'top', 'left', 'right', 'above', or 'below'), "relativeTo" (optional, key name of another dock; position relative to another dock), size [(xlength,ylength); note that lengths arguments are only a suggestion; docks will still have to fill the entire dock area and obey the limits of their internal widgets], "labels" (dict of position:str), "title" (str). '''
    
    docks = {
    'plot1' : {'type': 'plot1D' , 'position': 'left' , 'size': (500,500), 'labels':{'bottom':'Time (arb. units)','left':'Intensity (arb. units)'}},
    'phase_space' : {'type': 'plot2D', 'position': 'right', 'size': (300,300)},
    'plot2' : {'type': 'plot1D' , 'zoomOf': 'plot1'  , 'position': 'bottom', 'relativeTo': 'phase_space', 'size': (300,100)},
    'plot3' : {'type': 'plot1D', 'position': 'top','relativeTo':'phase_space', 'size': (300,300)},
    'custom_name' : {'type': 'image', 'position': 'above','relativeTo':'plot3', 'size': (300,300)},
    }
    
    return docks

def load_variables():
    
    ''' Returns a dict of the variables. Each variable is a dict with keys: "type" (e.g. np.float64, np.complex128), "init_cond" (type), "plot" (bool, optional default is True), "dock" (list of key name(s) of docks [str] as defined in load_dock function; optional; if not provided, will be ploted on every plot), "equation" (callable, optional default is diff_eq_{variable_name}), "help" (str, to be displayed in help message). Additionnal keys are added internally: "value", "observable" (False), "lineedit", "checkbox". '''
    
    variables = {
    'A'  : {'type': np.complex128, 'init_cond': 0., 'plot': False, 'dock':['plot1','plot2'], 'help':'field in the first cavity'},
    'B'  : {'type': np.complex128, 'init_cond': 0.001, 'plot': False, 'equation': diff_eq_B}
    }
    
    return variables

def load_observables():
    
    ''' Returns a dict of the observables. Similar to variables, observables are added internally to the dictionnary of variables. Each observable is a dict with keys: "type" (e.g. np.float64, np.complex128), "init_cond" (type), "plot" (bool, optional default is True), "dock" (list of key name(s) of docks [str] as defined in load_dock function; optional; if not provided, will be ploted on every plot), "equation" (callable, optional default is eq_{variable_name}), "calculation_size" (bool, whether you want according variable to be only the size of what calculation returns; WARNING: those items won't be stored), "help" (str, to be displayed in help message). Additionnal keys are added internally: "value", "observable" (True), "lineedit", "checkbox". '''
    
    observables = {
    'mod_A' : {'type': np.float64, 'init_cond': 0., 'plot': True, 'dock':['plot1','plot2'], 'help':'modulus square of A'},
    'mod_B' : {'type': np.float64, 'init_cond': 0., 'dock':['plot1','plot2','plot3']},
    'mod_A_2' : {'type': np.float64, 'init_cond': 0., 'plot': True, 'dock':[{'phase_space':['mod_A_2','mod_B_2']}],'calculation_size':True, 'help':'abs(A)**2 shorter to be plotted in phase space'},
    'mod_B_2' : {'type': np.float64, 'init_cond': 0. ,'dock':[{'phase_space':['mod_B_2','mod_A_2']}],'calculation_size':True},
    'mod_A_2D' : {'type': np.float64, 'init_cond': 0. ,'dock':['custom_name'],'calculation_size':True,'help':'variable to be used plotted in image'},
    #'ph_A' : {'type': np.float64, 'init_cond': 0., 'dock':['plot3']},
    #'ph_B' : {'type': np.float64, 'init_cond': 0., 'dock':['plot3']}
    }
    
    return observables


def load_params():
    
    ''' Returns a dict of the parameters. Similarly to variables/observables, each parameter has a dictionnary as "value" with keys: "init_cond" (float), "min" (float), "max" (float), step (float or int; WARNING if int this parameter will be an integer), "help" (str, to be displayed in help message). Additionnal keys are added internally: "value", "spinbox", "slider", "slider_conversion_factor". '''
    params = {}
    params['delta'] = {'init_cond': -8., 'min': -10., 'max': 10., 'step': 0.01, 'help':'detuning parameter'}
    params['f']     = {'init_cond': 4.8, 'min': 0.  , 'max': 20., 'step': 0.01}
    params['kappa'] = {'init_cond': 2.8, 'min': 0.  , 'max': 10., 'step': 0.01}
    params['gamma'] = {'init_cond': 0. , 'min': 0.  , 'max': 10., 'step': 0.01}
    params['tau']   = {'init_cond': 1. , 'min': 0.  , 'max': 10., 'step': 0.01}
    params['npts_PS'] = {'init_cond': 1000 , 'min': 1  , 'max': 2000, 'step': 1}
    params['folding']     = {'init_cond': 100 , 'min': 1  , 'max': 1000, 'step': 1}
    
    return params

# BEGIN Declaration of the equations. Automatically recognized pattern are "diff_eq_{variable}" (variables) and "eq_{observable}" (observables); with a name after the pattern that must match the variable/observable's one. Alternatively, you may use custom equation names. You should declare it in the variable/observable dictionnary with keyword "equation".

def diff_eq_A(ui,variables, params):
    return 1j*(params['delta']*params['tau'] + abs(variables['A'])**2)*variables['A'] - variables['A'] + (1j*params['kappa'] + params['gamma'])*params['tau']*variables['B'] + params['f']

def diff_eq_B(ui,variables, params):
    return 1j*(params['delta']*params['tau'] + abs(variables['B'])**2)*variables['B'] - variables['B'] + (1j*params['kappa'] + params['gamma'])*params['tau']*variables['A'] + params['f']

def eq_mod_A(ui,variables,params):
    return abs(variables['A'])**2
def eq_mod_B(ui,variables,params):
    return abs(variables['B'])**2
def eq_mod_A_2(ui,variables,params):
    return variables['mod_A'][-params['npts_PS']:]
def eq_mod_B_2(ui,variables,params):
    return variables['mod_B'][-params['npts_PS']:]
def eq_mod_A_2D(ui,variables,params):
    folding = params['folding']
    nb_rt   = int(len(variables['mod_A'])/params['folding'])
    return np.reshape(variables['mod_A'][-(folding*nb_rt):],(nb_rt,folding))
#def eq_ph_A(variables,params):
    #return [cm.phase(temp) for temp in variables['A']]       #np.array(np.arctan2(np.imag(variables['A']), np.real(variables['A'])))
#def eq_ph_B(variables,params):
    #return [cm.phase(temp) for temp in variables['B']]


def keyboard_keys():
    """ Returns a dictionnary of user defined keys of form key:callable. System reserved keys: [" ", "q", "h", "s", "r", "i", "c"]. This must return an empty dict if no extra keys. """
    
    keys = {
    't': extra_key,
    }
    
    return keys
    #return {}

def extra_key(variables,params):
    print('begin extra key t pressed')
    print(params)
    print('end extra key t pressed')

def kernel_my_own(variables,params):
    
    ''' Takes as arguments dicts of variables and params as {'key':value}. Returns a dict of the results with the same form. For now the function name must start with "kernel_" '''
    
    pass
