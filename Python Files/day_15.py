def file_reverser(file):
    '''
    A function named file_reverser which reverses the the lines and string in each line

    Parameter: file, a txt file which contains lyrics of song

     A txt file saved as file_name.txt which reverses all lines and character in each reversed line will
     be created after running the program

     Returns: The function doesn't return anything.
    '''
    with open(file) as f: # Opens the file in read mode
        file_ = f.readlines() # Saves all text in a variable file_ where each line is a list and closes the file when done.

    file_ = [j[:-2] for j in file_][::-1]  # Reverses the line in the file 
    lines  = [j[::-1]+'\n' for j in file_] # Reverses each element in each line


    with open('file_name.txt', 'w') as f: # Opens a new file and save t as file_name.txt in write mode
        f.writelines(lines) # Writes  the variable lines to the file

