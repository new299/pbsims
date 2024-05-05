import subprocess
import time
import sys

# Function to execute the external script and pipe output to a file
def execute_script(a, b, c, output_file):
    command = f"bash ./simrun {a} {b} {c}"
    with open(output_file, 'a') as f:
        subprocess.run(command.split(), stdout=f, stderr=subprocess.STDOUT)

# Function to print contents of a file
def print_file_contents(file_name):
    with open(file_name, 'r') as f:
        print(f.read())

# Main loop
start_a = 0
start_b = 0.0
start_c = 0.0
increment = 0.01
num_iterations = 10  # Change this to the number of loops you want

output_file = 'sim_output.txt'
summary_file = 'sim.summary_identity_stats.csv'

import csv

# Function to parse the CSV and extract identity value
def extract_identity(csv_file):
    identity = -1
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            identity = row['identity']
    return identity 

mis =0.0
dels=0.0
ins =0.0

while dels < 0.1:
    while ins < 0.1:
        execute_script(mis, ins, dels, output_file)
        err = extract_identity(summary_file)
        
        print(err, " ", end='')
        sys.stdout.flush()
        ins += 0.01
    dels += 0.01
    ins = 0
    print()
