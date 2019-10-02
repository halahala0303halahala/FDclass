# coding: utf-8
get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy.random import randint
from numpy.random import choice
l0 = randint(3,6)
for i in range(l0):
    l1 = randint(4,7)
    l2 = choice(words,l1)
    print(" ".join(l2))
