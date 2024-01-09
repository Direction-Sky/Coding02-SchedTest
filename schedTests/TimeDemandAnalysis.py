import numpy as np
import math
import include.TasksHelper as TH

# The tasks is an Array with three columns and n Rows
# Each Row represents one Task
# The columns hold the Tasks parameters
# column 0 is period P,
# column 1 is deadline D
# column 2 is WCET C
# P_i is accessed as: tasks[i][0]
# D_i is accessed as: tasks[i][1]
# C_i is accessed as: tasks[i][2]
# The number of tasks can be accessed as: tasks.shape[0]

# Will return the Workload or -1 if not feasible
def Workload(tasks, i, t):
    return -1

# Time demand function
# Returns the time-demand value of i-th task from a task set based on inference from higher-priority tasks.
# This function does not guarantee convergence
def w(tasks, i):
    
    # The first task has the highest priority, therefore no inference.
    if(i == 0):
        return TH.C_i(tasks, i)
    
    # First variable to check for convergence
    lastResult = TH.C_i(tasks, i)

    # The loop is exited when the relative deadline is exceeded
    while(lastResult < TH.D_i(tasks, i)):

        # Second variable to check for convergence
        newResult = TH.C_i(tasks, i)
        for j in range(i):
            # Inference from higher-priority tasks
            newResult += math.ceil(lastResult / TH.P_i(tasks, j)) * TH.C_i(tasks, j)

        # When convergence is found, we can stop and call this the final value
        if(newResult == lastResult):
            return newResult
        
        # Update the time demand at the end of each iteration
        lastResult = newResult

    # This is only called when the deadline is exceeded
    return lastResult

# The Time Demand Analysis Test
# Idea is to check whether all tasks can meet their deadlines given their time demand values
# If the time demand of each task does not exceed the relative deadline
def test(tasks):
    
    # Sort the tasks according to priority: shorter period means higher priority
    sorted_tasks = sorted(tasks, key=lambda task: task[0])

    # Iterate through the whole task set
    for i in range(len(sorted_tasks)):

        # Compare each time demand value with respective deadline
        if(w(sorted_tasks, i) > TH.D_i(sorted_tasks, i)):
            return False
    return True
