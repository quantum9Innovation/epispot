import epispot as epi  # load the epi-spot package


# variables (used when defining layers)


# basic reproductive number
def R_0(t):
    # we use a simple logistic function to model R_0 in this example
    return 2 - (2 / (1 + 2 ** (-t + 60)))  # these functions can be time-dependent


# all other variables are not time dependent (this is not required)


# recovery rate
def gamma(t):
    return 0.2


# total population
def N(t):
    return 1e+5


# probability of recovering
def p_recovery(t):
    return 1.0


# layers
Susceptible = epi.comps.Susceptible(0, 3, 0.2, 1e+5)  # Susceptible layer
Infected = epi.comps.Infected(1, 1e+5, R_0=3, gamma=0.2, p_recovery=1, recovery_rate=0.2)  # Infected layer
Recovered = epi.comps.Recovered(2, p_from_inf=1, from_inf_rate=0.2)  # Recovered layer

# the blank array in `layer_map` symbolizes that the Recovered layer has no further layers
Model = epi.models.Model(1e+5, layers=[Susceptible, Infected, Recovered], layer_names=['Susceptible', 'Infected',
                                                                                       'Recovered'],
                         layer_map=[[Infected],
                                    [Recovered], []])

epi.models.export(Model, 'model.yml')