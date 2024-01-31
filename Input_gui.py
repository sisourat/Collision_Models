import PySimpleGUI as sg
from models import *

def input_gui():
 defaults = ["13.6","0.529","1.0","1.0","4.5","1","16.0"]
 labels = ('Target Ionization Energy (eV):', 'Target electron radius (Angstrom):',
          'Target  mass (amu):', 'Target electron velocity (au):',
          'Target polarizability (Bohr^3)', 'Projectile charge:', 'Projectile mass (amu):')
 size = max(map(len, labels))

 font = ('Courier New', 11)
 sg.theme('DarkBlue4')
 sg.set_options(font=font)

 layout = [
             #              [sg.Text(label, size=size), sg.Input(defaults[i], key=label.split()[0])]
             [sg.Text(label, size=size), sg.Input(defaults[i], key=label)]
             for i, label in enumerate(labels)] + [
             [sg.Push(), sg.Button('Send')]
         ]
 window = sg.Window('Collision Model Input', layout)

 while True:
    event, values = window.read()
    model_cross_sections(labels,values)
    if event == sg.WIN_CLOSED:
        break

 window.close()
 return 0
