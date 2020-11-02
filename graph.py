from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib import pyplot as plt 
from matplotlib.figure import Figure

import sys
import seaborn as sns


class GraphWidget(FigureCanvas):

    def __init__(self):
        self.fig = Figure()
        self.canvas = self.fig.add_subplot(111)

        super().__init__(self.fig)

        