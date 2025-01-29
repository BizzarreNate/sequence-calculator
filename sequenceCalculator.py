from itertools import product
def generate_combinations(sequence, replace_chars, options):
    # Find all positions of the replacable characters
    positions = [i for i, char in enumerate(sequence) if char in replace_chars]

    # Generate all possible replacements for the positions
    replacements = list(product(options, repeat=len(positions)))

    #Generate and print all possible combinations
    for replacement in replacements:
        new_sequence = list(sequence)
        for pos, char in zip(positions, replacement):
            new_sequence[pos] = char
        print(''.join(new_sequence))

# Where you put the combination
sequence = "QEXXEQXX" # Characters to replace
replace_chars = "X"  #options to replace them with
options = "QE"

generate_combinations(sequence, replace_chars, options)