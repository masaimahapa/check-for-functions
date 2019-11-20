import re

def get_functions(code_path):
    print(code_path)
    with open(code_path) as f:
        code= f.readlines()
        func_names=[]
        for line in code:
            if line.startswith('def'):
                func= check_function(line)
                if func:
                    func_names.append(func)
        
        return func_names
            
def check_function(line):
    m= re.findall(r'(?<=def).*:', line)

    if m:
        func_name= m[0]
        func_name= func_name.split('(')[0].lstrip()
        return func_name

print(get_functions('calculator.py'))

