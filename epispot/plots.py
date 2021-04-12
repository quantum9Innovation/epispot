"""
The 'plots' module contains all plotting functions for visualizing models.
These functions require the installation of matplotlib for graphics.

## Structure:

- plot_comp_nums
"""

from . import plot
from . import random


def plot_comp_nums(Model, timesteps, starting_state=None, seed=100):
    """
    This is meant for plotting the number of people in each compartment over a period of time

    - Model: an instance of the `Model` class
    - timesteps: timesteps to plot as range(beg_time, end_time, day_length)
    - starting_state: initial conditions vector: [comp_1_start, comp_2_start, ...]
    - seed: =100, for generating new random colors
    - return: matplotlib plot
    """

    integral = Model.integrate(timesteps, starting_state=starting_state)
    compartments = []

    for _ in integral[0]:
        compartments.append([])

    for timestep in integral:
        for compartment in range(len(timestep)):
            compartments[compartment].append(timestep[compartment])

    DataFrame = {Model.layer_names[name]: compartments[name] for name in range(len(Model.layer_names))}
    fig = plot.line(DataFrame, title='Compartment Populations over Time')
    fig.show()

