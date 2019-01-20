# Human Statistics: Heuristic Average
## Code to implement a heuristic average similar to the way a human would evaluate the average of a suite of numbers

## Tests
### Replicates the statistical average when there is no weight given to interpretation weights

test_in = [1,2,3,2,5,6,2,3,2,2,1,2,4,5,6,2,2]

test_out = sum(test_in)/len(test_in)

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


## Functional specification
'''
Function uses a reward function on a series of values in a list to assign a weight to each of them, with 1 being the basic value and
the reward increasing with the number of times that value has already occurred in the series. This is intended to imitate a human 
heuristic habit of giving undue weight to repeated values when determining the average of a series
'''

def freq_reward(values):
    ''' Iterates through the list and updates the weights in a parallel list to reflect how frequently that element has been seen '''
    weights = []
    for i in range(len(values)):
        repeats = 1
        for j in values[:i]:
            if j == values[i]:
                repeats += 1
        weights.append(repeats)
    return(weights)

def no_reward(values):
    weights = []
    for i in range(len(values)):
        weights.append(1)
    return(weights)

def dot_prod(v1, v2):
    output = []
    for i, j in zip(v1, v2):
        output.append(i*j)
    return sum(output)

def heuristic_avg(values, reward_func):
    weights = reward_func(values)
    product = dot_prod(weights, values) 
    average = product/ sum(weights)
    return average
    