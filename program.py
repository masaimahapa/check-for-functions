import re

def get_functions(code_path):
    """
    takes in a path to a python file. 
    return: dictionary of functions in the file.
    """
    
    if code_path[-3:]=='.py':
        #if the last 3 characters of the filename is .py, then its a python file.
        dict_function= {}
        ls_functions=[]
        in_function=False

        with open(code_path) as f:
            #open the file with a context manager
            code= f.readlines()
            func_names=[]
            for idx, line in enumerate(code):
                #read every line in the code and have a counter 
                if line.startswith('def'):
                    func= check_function(line)

                    #if a line is a function
                    if func:
                        #func_indentation= 4
                        start_row= idx+1
                        func_names.append(f'name: {func} start_row: {start_row}')
                        dict_function['name']= func
                        dict_function['start_row']=start_row
                        
                        #Condtion if line is within a function
                        in_function= True
                        

                if not line.startswith('def'):
                    code_indent= len(line)- len(line.lstrip())


                    if code_indent<=1 and in_function is True:
                        in_function= False
                        end_line= idx
                        dict_function['end_row']=end_line
                        ls_functions.append(dict_function)
                        dict_function={}
                        
                    #if idx== start_row+1:
                    #    func_indentation= len(line)- len(line.lstrip())
    else:
        raise TypeError('Not a python file')
                
    return ls_functions
            
def check_function(line):
    #look for definition in a given line of code.
    m= re.findall(r'(?<=def).*:', line)

    if m:
        #if there are function definitions found
        func_name= m[0]
        func_name= func_name.split('(')[0].lstrip()
        #return the name of a function
        return func_name

print(get_functions('calculator.py'))

