import sys

# Check if the filename is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

def replace_numbers_with_zero(element):
    # Split the element by commas
    parts = element.split(',')

    # Identify and replace numbers with 0
    for i in range(3, len(parts)):
        parts[i] = '10'

    # Join the parts back together
    return ','.join(parts)

# Open the file
with open(filename, 'r') as file:
    # Read each line
    for line in file:
        # Split the line by tabs
        elements = line.strip().split('\t')

        for i in range(len(elements)):
            if elements[i].startswith('ip:'):
                elements[i] = replace_numbers_with_zero(elements[i])

            if elements[i].startswith('pw:'):
                elements[i] = replace_numbers_with_zero(elements[i])

        # Print the elements separated by tabs
        print('\t'.join(elements))
