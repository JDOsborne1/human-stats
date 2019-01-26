# Human Statistics: Heuristic Average
## Code to implement a heuristic average similar to the way a human would evaluate the average of a suite of numbers

## Tests
### Replicates the statistical average when there is no weight given to interpretation weights
import statistics as st

test_in = [1,2,3,2,5,6,2,3,2,2,1,2,4,5,6,2,2]

test_out = sum(test_in)/len(test_in)

print(test_out == st.mean(test_in))

def test_1(func):
    test = func(test_in, no_reward) == test_out
    if test:
        print("Replicates statistical behaviour")
    else:
        print("Fails to replicate statistical behaviour")

### Gives a disproportional weight to the more frequent elements when there are interpretation weights

def test_2(func):
    out = func(test_in, freq_reward)
    test = (out > 2.0) & (out < test_out)
    if test :
        print("Shifts the statistical average in the correct direction without going too far.")
    else:
        print("Failed to move the statistical average in the right direction without overshooting")

### Gives extra weight to departures from the memorable past numbers

def test_3(func):
    out = func(test_in, surpise_reward)
    test = (out < 6) & (out > test_out)
    if test :
        print("Shifts the statistical average in the correct direction without going too far.")
    else:
        print("Failed to move the statistical average in the right direction without overshooting")

## Functional specification
'''Function uses a reward function on a series of values in a list to assign a weight to each of them, 
with 1 being the basic value and the reward increasing with the particular condition'''

def freq_reward(values):
    ''' Iterates through the list and updates the weights in a parallel list to reflect how frequently that element has been seen. 
    This is intended to imitate a human heuristic habit of giving undue weight to repeated values when determining the average of a series'''
    weights = []
    for i in range(len(values)):
        repeats = 1
        for j in values[:i]:
            if j == values[i]:
                repeats += 1
        weights.append(repeats)
    return weights

def surpise_reward(values, m = 3):
    '''Implements a surprise reward function, where numbers are given weights which scale to how much they depart from the trailing average. which is the mean of the previous m values
    where m is a constant which is supposed to capture how far back in a sequence a human would be likely to remember a number'''
    weights = []
    for i in range(len(values)):
        if i < m:
            weight = 1
        else:
            weight = abs(values[i] - st.mean(values[i-m:i]))
        weights.append(weight)
    return weights


def no_reward(values):
    '''Implements a referece function, where there is no additonal reward given to the values, and the heuristic average becomes the statistical mean'''
    weights = []
    for i in range(len(values)):
        weights.append(1)
    return weights

def dot_prod(v1, v2):
    '''Implements the dot product for lists, could be replaced with a method overload for lists at a later date. But this way is more explicit'''
    output = []
    for i, j in zip(v1, v2):
        output.append(i*j)
    return sum(output)

def heuristic_avg(values, reward_func):
    weights = reward_func(values)
    product = dot_prod(weights, values) 
    average = product/ sum(weights)
    return average
    