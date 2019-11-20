# 6-6 Average Of Numbers
# Shaun Hayworth
# CIS 2
# 11-19-2019
# Source code and revision history are available at
# https://github.com/SCHayworth/6-6-Average-Of-Numbers

# Calculates the average of a series of integers contained in the number.txt
# file and displays the result.


def main():
    '''Mainline program logic
    '''
    # Open the file numbers.txt in read mode.
    file_name = open('numbers.txt', 'r')

    # Initialize accumulators for the number of lines in the file, and the sum
    # of the values on each line.
    total_numbers = 0
    sum_of_numbers = 0

    # Read and process each line from the file.
    for line in file_name:
        # Convert the string to an integer and add it to the sum accumulator
        value = int(remove_space(line))
        sum_of_numbers += value
        # Increment the total numbers accumulator.
        total_numbers += 1

    # Close the numbers.txt file
    file_name.close()

    # Calculate and display the average of the values in the file.
    average = sum_of_numbers / total_numbers
    print(average)


def remove_space(string):
    '''Removes extra spaces from a string.
    '''
    return string.replace(" ", "")

# Call the main() function
main()
