# Open the file
with open('aa', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Remove newline character from the end of the line
        line = line.strip()
        
        # Print the first 20 characters
        print(line[:30], " ",line[-30:])
        

