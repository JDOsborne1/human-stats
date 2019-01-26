# human-stats
A set of functions which to implement statistical functions in a human-ized way

These functions are intended to give a better picture of the human statistical perceptions of a numeric problem


There is also scope for them to be used in the context of machine learning, where they can be used to form reward and punishment conditons which mimic human alert points.

## Production notes

### Human Average
I suspect that humans do not correctly implement the statistical mean when calculating the "average" of a set of numbers, 
instead a sort of heuristic hybrid of mean, mode and median are implemented, with special weight generally given to any 
numbers which would seem more significant to a human.

1. Frequency already seen
   The number of times a number has laready been seen by that point gives increased weight to the moving average. 
   * ~~Absolute previous frequency~~ (Implemented)
   * Decaying previous frequency (TODO)
2. Extreme values
   Values which deviate from an otherwise tightly packed group of numbers are given increased weight
   * absolute deviation (TODO)
   * scaled deviaton (TODO)
   * local deviation (TODO)
   * scaled local deviation (TODO)
