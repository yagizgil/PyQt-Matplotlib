from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

from matplotlib import pyplot as plt
import graph
import seaborn as sns

import numpy as np


class Screen(QWidget):

    def __init__(self):
        super().__init__()

        self.x = np.random.randn(1000).cumsum()
        self.y = np.random.randn(1000).cumsum()
        self.z = np.random.randn(1000).cumsum()

        self.setUI()

    def setUI(self):
        self.f = QFormLayout()
        
        self.cb = QComboBox()
        self.cb.addItems(['Solarize_Light2',
                        '_classic_test_patch',
                        'bmh',
                        'classic',
                        'dark_background',
                        'fast',
                        'fivethirtyeight',
                        'ggplot',
                        'grayscale',
                        'seaborn',
                        'seaborn-bright',
                        'seaborn-colorblind',
                        'seaborn-dark',
                        'seaborn-dark-palette',
                        'seaborn-darkgrid',
                        'seaborn-deep',
                        'seaborn-muted',
                        'seaborn-notebook',
                        'seaborn-paper',
                        'seaborn-pastel',
                        'seaborn-poster',
                        'seaborn-talk',
                        'seaborn-ticks',
                        'seaborn-white',
                        'seaborn-whitegrid',
                        'tableau-colorblind10'])
        self.cb.currentIndexChanged.connect(self.change)
        self.f.addRow(self.cb)

        self.ch = QCheckBox("Seaborn")
        self.ch.clicked.connect(self.setsea)
        self.f.addRow(self.ch)

        self.setGraph()

        self.setLayout(self.f)

    def change(self):
        plt.style.use(self.cb.currentText())
        self.setGraph()

    def setGraph(self):
        try:
            self.f.removeRow(self.g)
        except:
            pass
        self.g = graph.GraphWidget()

        self.g.canvas.plot(self.x)
        self.g.canvas.plot(self.y)
        
        self.g.canvas.legend(["X Ekseni","Y Ekseni"],loc="best")

        self.f.addRow(self.g)

    def setsea(self):
        if self.ch.isChecked():
            sns.set()
        else:
            sns.reset_defaults()
        
        plt.style.use(self.cb.currentText())
        self.setGraph()