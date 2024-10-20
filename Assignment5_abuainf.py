''' COMPSCI Assignment 5: Functions for Cleaning Data for Machine Learning Classification.
Function 1 reads a file and returns a two-dimensional list containing rows and columns of floating point
numbers, as well as 'None' values where floats are not applicable.
Function 2 writes the data contained in a two-dimensional list into a new file.
Function 3 deletes rows containing bad data (i.e. 'None' values) in a two-dimensional list.
Function 4 replaces 'None' values in a two-dimensional list with the average value for that row.
Test program at end of code tests these four functions on numerical data in 'wbcd.csv'.
Faris Abuain, June 2024, McMaster University.'''


## Read_CSV Function.

def read_csv(filename):
    '''read_csv: reads a csv file and produces a 2d list of data.

    Parameters:
        filename: string which represents a file name.
        
    Returns:
        False: if exception is raised.
        floats_list: 2d list of csv data.
        
    Outputs:
        none
    '''
    
    
    floats_list = [] # initiate two-dimensional-list to contain data in file
    
    try:
        file = open(filename)
        
    except FileNotFoundError: # returns 'False' if a file with 'filename' cannot be found
        return False
    
    lines = file.readlines() # creates list of strings, with each string representing a row
    
    file.close()
    
    for line in lines: # iterates through each row
        line_list = line.split(',') # turns each row into a list of strings, split along commas (as this is a csv file)
        for i in range(len(line_list)):
            try:
                line_list[i] = float(line_list[i]) # converts each entry in row list into a float
            except ValueError:
                line_list[i] = None # if converting to a float raises an exception, entry is replaced with 'None'
        floats_list.append(line_list) # the lists of row data are appended to the two-dimensional list, row by row
        
    return floats_list
    
## Write_CSV Function.

def write_csv(filename, two_dimensional_list):
    '''write_csv: writes the data in a 2d list to a csv file.

    Parameters:
        filename: string which represents a file name.
        two_dimensional_list: a 2d list, columns and rows.
        
    Returns:
        True: if file-writing works.
        False: if exception is raised during file_writing.
        
    Outputs:
        none
    '''
    
    try: 
        file = open(filename, 'w') 
        for lists in two_dimensional_list:
            file.write((','.join((str(s) for s in lists)))) # convert each entry to a string and separate with commas (csv format)
            file.write('\n') # before moving to next row, we perform a carriage return
        file.close() # close file before proceeding
        return True
    
    except:   # if an exception of any kind is raised *at any point* in file-writing process, return 'False'
        return False
    
## Clean_Del Function.

def clean_del(two_dimensional_list):
    '''clean_del: removes rows containing bad data.

    Parameters:
        two_dimensional_list: a 2d list, columns and rows.
        
    Returns:
        new_list: a new 2d list with rows containing bad data removed.
        
    Outputs:
        none
    '''
    
    new_list = []  # new list is defined, as we will not be modifying the original data
    
    for lists in two_dimensional_list:
        
        if None not in lists:
            new_list.append(lists) # this creates a new list with rows of original list which did *not* contain bad data (i.e. 'None')
        
    return new_list

## Clean_Avg Function.

def clean_avg(two_dimensional_list):
    '''clean_avg: replaces bad values with the average for that row of data.

    Parameters:
        two_dimensional_list: a 2d list, columns and rows.
        
    Returns:
        new_list: a new list where 'None' entries of original list are replaced with row average.
        
    Outputs:
        none
    '''
    
    new_list = [] # new list is defined, as we will not be modifying the original data
    
    
    for lists in two_dimensional_list:
        
        temp_list = [x for x in lists if x is not None] # creates a temporary list containing all numeric values in a row
        avg = sum(temp_list) / len(temp_list) # use this temporary list to calculate average for row
        
        if None not in lists:
            new_list.append(lists) # append row to list if no modifications need to be made
        else:
            modified_list = [] # create a modified row
            for i in range(len(lists)):
                if lists[i] == None:
                    modified_list.append(avg) # replace 'None' values with average for row
                else:
                    modified_list.append(lists[i]) # otherwise, same values as original row
            new_list.append(modified_list) # add modified row to new list
        
    return new_list

## Test Program

## defining each list of data (original, and the two modified)

data_list = read_csv('wbcd.csv') ## (OCTOBER 2024) Comment for clarification: 'wbcd.csv' is a test file provided by Professor. Uploaded to this repository for demonstration.

clean_del_data_list = clean_del(data_list)

clean_avg_data_list = clean_avg(data_list) 

## writing each set of data to a new file

write_csv('wbcd_orig.csv', data_list)

write_csv('wbcd_del.csv', clean_del_data_list)

write_csv('wbcd_avg.csv', clean_avg_data_list)





