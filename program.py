import re

def list_all_js_function_names(code_path):
    """
    takes in a path to a python file. 
    return: dictionary of functions in the file.
    """
    
    if code_path[-3:]=='.js':
        #if the last 3 characters of the filename are .js, then its a javascript file.
        dict_function= {}
        ls_functions=[]
        in_function=False

        with open(code_path) as f:
            #open the file with a context manager
            code= f.readlines()
            func_names=[]
            for idx, line in enumerate(code):
                #read every line in the code and have a counter 
                if 'function' in line: 
                    
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
                        

                if not line.startswith('function'):
                    code_indent= len(line)- len(line.lstrip())


                    if code_indent==0 and in_function is True and line.startswith('}'):
                        in_function= False
                        end_line= idx+1
                        dict_function['end_row']=end_line
                        ls_functions.append(dict_function)
                        dict_function={}
                        
                    #if idx== start_row+1:
                    #    func_indentation= len(line)- len(line.lstrip())
    else:
        raise TypeError('Not a javascript file')
                
    return ls_functions
            
def check_function(line):
    #look for definition in a given line of code.
    line= line.lstrip()
    if line.startswith('function '):

        m= re.findall(r'(?<=function ).*\(', line)
        m=m[0][:-1]

    elif 'function' in line:
        m= line.split('=')[0]
    else: 
        return None
        


    return m.strip()

print(list_all_js_function_names('cards.js'))


