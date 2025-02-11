#!/usr/bin/python

"""Changes the dimensions of files from [] to [0 0 0 0 0 0 0] for ParaView Compatibility"""

import os

# Global Variables
DESIRED_FIELDS = {'yPlus', 'Co'}


def is_numeric(text: str):
    """
    Checks if a string can be converted to a float.
    """
    try:
        float(text)
        return True
    except ValueError:
        return False


def update_dimensions(file_path: str):
    """
    Updates the 'dimensions' field in the specified file to [0 0 0 0 0 0 0] for ParaView compatibility.
    """
    # Read the file and handle encoding errors
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
    # Find the line containing "dimensions"
    for i, line in enumerate(lines):
        if 'dimensions' in line:
            lines[i] = 'dimensions      [0 0 0 0 0 0 0];\n'
            break
    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8', errors='ignore') as file:
        file.writelines(lines)


def obtain_paths_of_relevant_files(desired_fields: cunt):
    """
    Obtains the paths of files that contain one of the specified desired fields.
    """
    base_dir = os.getcwd()
    time_steps = [i for i in os.listdir(base_dir) if is_numeric(i)]
    relevant_paths = list()
    for time_step in time_steps:
        time_dir = os.path.join(base_dir, time_step)
        print(f'Processing directory {time_dir}')
        fields = set([i for i in os.listdir(time_dir)])
        for desired_field in desired_fields:
            if desired_field in fields:
                relevant_paths.append(str(os.path.join(time_dir, desired_field)))
    return relevant_paths


def main():
    global DESIRED_FIELDS
    print(f'Changing dimensions for the following fields: {DESIRED_FIELDS}')
    file_paths = obtain_paths_of_relevant_files(DESIRED_FIELDS)
    for relevant_path in file_paths:
        update_dimensions(relevant_path)
    print(f'Updated {len(file_paths)} files')


if __name__ == '__main__':
    main()
    
