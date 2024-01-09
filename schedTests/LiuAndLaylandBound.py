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

# The necessary Test for the Liu and Layland Bound
# This is the formula taken from slide 20 in 6.2
def test(tasks):
    # This bound was discovered by Liu and Layland
    # For n = 10, LLBound ≈ 0.71773
    LLBound = len(tasks) * (math.pow(2, 1/len(tasks)) - 1)

    # Sort the tasks according to priority: shorter period -> higher priority
    sorted_tasks = sorted(tasks, key=lambda task: task[0])

    U_total = TH.getTotalUtilization(sorted_tasks, len(sorted_tasks))
        
    return U_total <= LLBound
