# PROBLEM DESCRIPTION
"""
factor of 2 approximate solution for the knapsack problem

GIVEN:
K: int
n: list[real numbers]

RETURN:
solution: list[real numbers]
"""

import random # TESTING
TESTING = False

# IMPLEMENTATION + PSUEDOCODE
# init n and K variables
n = [9.3, 24, 14, 5, 8, 17, 4.2] # EXAMPLE GIVEN
K = 20 # EXAMPLE GIVEN

# iterate over items
def main():
    # testing used for correctness, not part of alg implementation
    if TESTING:
        for i in range(10000):
            testing_n = []
            for _ in range(random.randrange(1, 1000)):
                testing_n.append(random.randint(1, 1000))
            testing_K = random.randint(0, 1000)

            list = knapsack_approx(testing_n, testing_K)
            print(f"n: {testing_n}\nK: {testing_K}\nsolution: {list}") #DEBUG
            assert list != ["ERROR"], f"No solution found for \nk: {testing_K}\nn: {testing_n}"
    # END TESTING
    print(f"n: {n}\nK: {K}\nsolution: {knapsack_approx(n, K)}")

def knapsack_approx(n, K):
    # init variables to track a running total and what values have been added to get said total
    solution = []
    total = 0
    # iterate over list n
    for real_number in n:
        # if number in n is greater than or equal to K / 2 and smaller than or equal to K. Return it, as it is a valid solution
        if real_number >= K / 2 and real_number <= K:
            return [real_number]
        # if running total + real_number <= K, add to total and keep track of number added in "solution"
        if total + real_number <= K:
            total += real_number
            solution.append(real_number)
            # if total >= K / 2, return the "solution" variable (numbers added to be greater than K / 2 and smaller than K)
            if total >= K / 2:
                return solution
    if TESTING:
        return ["ERROR"]
    
main()

# CORRECTNESS
"""
The algorithm above is a factor of 2 approximate solution as it searches for individual items with a value between K/2 and K
If the value added to the running total falls below K then it is added to the solution
If the solution is greater than or equal to K/2 after added the value then the solution is returned and the program terminates

Testing for this correctness was done by randomly generating lists of various lengths and randomly generating K
When a solution was not found, the chosen n and K values were manually reviewed for a potential missed solution
"""

# TIME ANALYSIS
"""
O(n)
algorithm takes linear time as it only iterates over the list of values n once
"""
