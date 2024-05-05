import random

def read_sequence_from_file(filename):
    with open(filename, 'r') as file:
        sequence = file.read().strip()
    return sequence

def generate_random_subsequence(sequence, subsequence_length):
    start_index = random.randint(0, len(sequence) - subsequence_length)
    return sequence[start_index:start_index + subsequence_length]

# Example usage
filename = "phix.flat"  # Update with your file name
sequence = read_sequence_from_file(filename)
subsequence_length = 1000

# Generate and print 5 random subsequences
for i in range(1000):
    random_subsequence = generate_random_subsequence(sequence, subsequence_length)
    print(f"{random_subsequence}")

