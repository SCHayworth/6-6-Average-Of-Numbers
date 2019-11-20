# 6-6-Average-Of-Numbers
 Reads a series of integers in a file and averages them.

## Scope
Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk. Write a program that calculates the average of all the numbers stored in the file.

## Requirements
Use a for loop. If you use two accumulators, one can keep track of the number in the series and one can sum the numbers as they are read. And, the str will need to be converted to a float before calculating.

## Pseudocode
### Main program logic
    START
      SET sum accumulator to 0
      SET numbers accumulator to 0
      OPEN numbers.txt
      FOR each line in numbers.txt
        CONVERT string on line to an integer
        ADD value to sum accumulator
        INCREMENT numbers accumulator by 1
      ENDFOR
      CLOSE numbers.txt
      CALCULATE average = sum divided by numbers
      PRINT average
    END
