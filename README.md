# GUIDE
Graphical User Interface for Differential Equations

This package is made for simulating and interfacing differential equations using PyQt and pyqtgraph. The main code is located in GUIDE.py and is in charge of loading a user input.py file and creating the Graphical User Interface (parameters, variables, etc. and associated sliders, checboxes, keyboard keys, etc.) dynamically. The file GUIDE.ui is a layout of the graphical interface and each element (Tree, Dockarea, etc.) is filled by GUIDE.py. The user file input.py is the only file to be modified by the user. It contains definitions of the plots, the variables, the observables, the parameters and the associated equations (along with additional functionalities).

![alt text](https://github.com/bgarbin/GUIDE/blob/master/GUIDE_example.png?raw=true)

Note: - only ODE are supported at the moment

## Installation:
git clone https://github.com/bgarbin/GUIDE

## Usage
python GUIDE.py -f input.py

## Requirements:
- Python: >= 3.7

(To install any of the following simply type: pip install package_name. Note: on't forget to add the option --upgrade if package is already installed.)
- pyqtgraph: >= 0.11
- pyqt5: >= 5.11.2 (WARNING: if upgrading from an older version you seem to have to uninstall manually module sip [pip uninstall sip], version 5.11.2 and older use PyQt5-sip)
- openpyxl
- pandas

TODO:

      First:     WARNING think about what to provide to kernel and to keyboard_keys
      - verify unit of nstep_record and nstep_update_plot
      - Parameters: - introduce ramp or modulation
                    - add plot possibility and according checkbox
                    - add linked parameters ('equation' keyword for parameters)
      - PDE : - do this
              - variable values and re-optimize (direct indexation?)
      - Optimize: - each dock's plot in a remote plot widget
                  - calculation in a remote worker
                  - multi process calculation for multi-equations 
                  - calculation function written in fortran and pre-compiled
                  
      Secondary:
      - match plot2D colors with toggle
      - toggle for auto y axis
      - better "h" help
      - SAVE: - load state again
              - independant saving and calculation (for PDE) 
      - record: - at the begining remove the 10000 firsts points
      - astype for parameters specified as a 'type' keyword
