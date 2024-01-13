# Some elevators bottom out at the first floor and some at the (P)arking garage.
# Given how many of each type of elevator there are, determine probability that calling an elevator will let you get to the basement.
# The building is n stories tall and x% of people on each story want to get to the first floor, meaning their elevator will stop to pick you up if you are on a floor below them.

# Constraints:
# Number of elevators in building
# Number of elevators that go to P
# Number of floors above you

# Need:
# likelihood that someone is calling the elevator above you
# likelihood that the elevator that arrives goes to P

import numpy as np

#region Inputs
num_simulations = 1_000
num_residents = 500
num_floors = 15
num_elevators_G = 2
num_elevators_P = 1

call_floor = 5  # floor you're getting the chance for
#endregion

#region Framing Vars and classes
bool_arr = [True, False]  # to pull random bool with numpy
results = []


class Elevator:
    def __init__(self, position, lowest_floor):
        self.position = position
        self.lowest_floor = lowest_floor

    travelling_down = np.random.choice(bool_arr)
    current_floor = np.random.randint(0, num_floors)  # random starting floor from 0 (P) to highest
#endregion


for i in range(num_simulations):
    #region Creating array of elevators
    elevators = []

    for j in range(0, num_elevators_G):
        elevators.append(Elevator(j, "G"))
    for j in range(0, num_elevators_P):
        elevators.append(Elevator(num_elevators_G+j, "P"))
    #endregion

    responding_elevators = np.random.choice(elevators, 3, replace=False) # randomize order in which elevators are responding to call

    filled = False

    while not filled:
        for j in responding_elevators:
            if j.travelling_down == True and j.current_floor >= call_floor:
                results.append(j)
                filled = True
                break
            else:
                j.travelling_down = True
                j.current_floor = num_floors # after going down once, the elevator would go to the highest floor someone called it from, meaning your floor or higher

numerator = 0
for i in results:
    if i.lowest_floor == "P":
        numerator += 1

print('Chance of getting to basement (P)arking:', 100*numerator/len(results))
