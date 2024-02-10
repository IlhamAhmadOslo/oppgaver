# -*- coding: utf-8 -*-
"""
Created on Sat May 28 14:42:07 2022

@author: Eier
"""

import textwrap
from biosim.simulation import BioSim

geogr = """WWW
           WLW
           WWW"""
geogr = textwrap.dedent(geogr)

ini_herbs = [{'loc': (2, 2),
              'pop': [{'species': 'Herbivore',
                       'age': 5,
                       'weight': 20}
                      for _ in range(50)]}]

for seed in range(100, 103):
    sim = BioSim(geogr, ini_herbs, seed=seed,
                 img_base='../results/mono_ho_{:05d}'.format(seed))
    sim.simulate(301, img_years=300)