"""
Project: ENGER conlang
File: ENGER_program.py
Authors: Andre Oppenheimer, Dalia Carvalho Rodrigues, Jasper Schmidt
Date: 10.07.2025
Version: 1.0.0

Description:
    This script functions as the core program of the ENGER project.
    It generates words and let's the user apply phonological rules to them.

Dependencies:
    - dictionaries.py
    - word_generator.py
    - phon_rules.py

Repository:
    https://osf.io/4dfhs/

"""

from helper_functions_dictionaries import *
import ipywidgets as widgets
from IPython.display import display

clear_log()

word = build_word()
print(f"Your word is: {' '.join(word)}")

options = rule_possible_check(word)

output = widgets.Output()
display(output)

buttons = [widgets.Button(description=opt, layout=widgets.Layout(width="250px", height="40px")) for opt in options]

for btn in buttons:
    btn.on_click(make_handler(btn.description, word, output))
    display(btn)