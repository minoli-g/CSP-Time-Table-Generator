# CSP-Time-Table-Generator
Python code which uses backtracking to assign subjects to timeslots under certain constraints provided. 



## Problem description
Subjects are either compulsory or optional. 
Each subject has a set of associated time slots that it may be scheduled in.
A certain number of rooms are available for teaching. 
A single subject is taught in a single timeslot and room.


Two compulsory subjects cannot share the same timeslot
Subjects can share a timeslot (if at most one of them is compulsory) but not a room.

This problem can be modeled as a constraint satisfaction problem, with the two constraints given above.


Input - 
A CSV file which provides the subject and room names, and for each subject, its compulsory/optional status and possible timeslots. Sample inputs are provided.

Output - 
Prints the subject-timeslot-room mapping to the console. Also writes a CSV file to the location provided, showing each subject with its timeslot and room as scheduled by the algorithm.
If the problem is such that no solution can be found, prints a message to that effect. 


## Running the code

The Python code may be run from the command line, using the syntax shown
```
assign.py <path to input csv file> <path to desired output CSV write location>
 ```
 
 For example, in the root directory, run
 
 ```
 assign.py inputs/input1.csv outputs/myoutput.csv
 ```
 
 
 The .exe file was compiled from the Python source code using PyInstaller, and is run similarly.
 
  ```
  assign inputs/input1.csv outputs/myoutput1.csv
  ```

## References
For an explanation of Constraint Satisfaction Problems and the backtracking algorithm used in this code, see [CSC384 Lecture 04 - Backtracking Search(CSPs) - University of Toronto](https://www.cs.toronto.edu/~sheila/384/w11/Lectures/csc384w11-Lecture-04-Backtracking-Search.pdf)

