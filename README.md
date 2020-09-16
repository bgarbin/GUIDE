# GUIDE
Graphical User Interface for Differential Equations

This package is made for simulating and interfacing differential equations using PyQt and pyqtgraph. The main code is located in GUIDE.py and is in charge of loading a user input.py file and creating the Graphical User Interface (parameters, variables, etc. and associated sliders, checboxes, keyboard keys, etc.) dynamically. The file GUIDE.ui is a layout of the graphical interface and each element (Tree, Dockarea, etc.) is filled by GUIDE.py. The user file input.py is the only file to be modified by the user. It contains definition of the plots, the variables, the observables, the parameters and the associated equations (also additional functionalities).

Note: - only ODE are supported at the moment

## Installation:



## Requirements:
Python: >= 3.7
pyqtgraph: >= 0.11


TODO:

      First:     WARNING think about what to provide to kernel and to keyboard_keys
      - Parameters: - introduce ramp or modulation
                    - add plot possibility and according checkbox
                    - add linked parameters ('equation' keyword for parameters)
      - PDE : - do this
              - variable values and re-optimize (direct indexation?)
      - Parrallelize: - each dock's plot in a remote plot widget
                      - calculation in a remote worker
                      - multi process calculation for multi-equations 
       
      Secondary:
      - toggle for auto y axis
      - better "h" help
      - SAVE: - load state again
              - independant saving and calculation (for PDE) 
      - record: - at the begining remove the 10000 firsts points
      - astype for parameters specified as a 'type' keyword
