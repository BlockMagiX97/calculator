import sys

# iterative version

# operator
def add(values):
    result = 0
    for number in values:
        result += number
    return result

def minus(values):
    result = values[0]
    for number in values[1:]:
        result -= number
    return result

def multiply(values):
    result = values[0]
    for number in values[1:]:
        result *= number
    return result

def devide(values):
    result = values[0]
    for number in values[1:]:
        result /= number
    return result



# misc
def is_a_number(string):
    try:
        float(string)
        return True
    except:
        return False



# implements braclets
def find_braclet(num_string, offset):
    first_index = -1
    last_index = -1
    loc_number = 0
    for ch_i in range(len(num_string)):
        ch = num_string[ch_i]
        if ch == '(':
            if first_index < 0:
                first_index = ch_i
            loc_number += 1
            
        elif ch == ')':
            loc_number -= 1
        if loc_number <= 0:
            last_index = ch_i
            break
    return (first_index + offset, last_index + offset)

def find_pairs_of_bracelets(num_string):
    out = []
    for ch_i in range(len(num_string)):
        ch = num_string[ch_i]
        if ch == '(':
            out.append(find_braclet(num_string[ch_i:], ch_i))
    return out

def is_not_only_in_bracelets(num_string, operator):
    for ch_i in range(len( num_string)):
        ch = num_string[ch_i]
        if ch == operator:
            bracelets = not_in_bracelets(num_string, ch_i)
            if not_in_bracelets(num_string, ch_i):
                return True
    return False

def not_in_bracelets(num_string, index):
    last_index = float('-inf')
    first_index = float('inf')

    if '(' in num_string and ')' in num_string:
        bracelets = find_pairs_of_bracelets(num_string)
        for x in find_pairs_of_bracelets(num_string):
            first_index, last_index = x
            out = not (last_index > index and index > first_index)
            if not out:
                return False
    return True






# magic
def _calculate(num_string, operator, operator_function):

    pos = []
    for character_index in range(len(num_string)):
        ch = num_string[character_index]
        if ch == operator and not_in_bracelets(num_string, character_index):
            pos.append(character_index)
    out = [calculate(num_string[:pos[0]])]
    pre_x = pos[0]
    for x in pos[1:]:
        out.append(calculate(num_string[pre_x + 1:x]))
        pre_x = x
    out.append(calculate(num_string[pre_x + 1:]))

    return operator_function(out)

def calculate(num_string):
   

    if "+" in num_string and is_not_only_in_bracelets(num_string, '+'):
        return _calculate(num_string, "+", add)
    
    elif "-" in num_string and is_not_only_in_bracelets(num_string, '-'):
        if num_string[0] == '-':
            num_string = '0' + num_string
        return _calculate(num_string, "-", minus)

    elif "*" in num_string and is_not_only_in_bracelets(num_string, '*'):
        return _calculate(num_string, "*", multiply)

    elif "/" in num_string and is_not_only_in_bracelets(num_string, '/'):
        return _calculate(num_string, "/", devide)

    elif '(' in num_string and ')' in num_string:
        first_index, last_index = find_braclet(num_string, 0)
        return calculate(num_string[first_index + 1:last_index])
    
    
    elif is_a_number(num_string):
        return float(num_string)
    # debuging, if not here it will throw recursion depth error
    raise ValueError('I have no idea how i fucked up')
        








# Trash that will maybe be used.

sys.exit()
# recursive version
#   - uses some functions from above
#   - lacks:
#       - operator priority
#       - minus (use negative numbers for example +-)
#       - braclets
class Operators:
    def __init__(self):
        self.string_to_identifier = {"+": 0, "*": 1, "/": 2}

    def get_identifier_hashmap(self):
        return self.string_to_identifier

def is_a_operator(string):
    operators = Operators()
    if len(string) > 1:
        return False
    return string in operators.get_identifier_hashmap()

def choose_operator(string):
    operators = Operators()
    if is_a_operator(string):
        return operators.get_identifier_hashmap()[string]
        
def choose_opereting_function(operator_identifier):
    if operator_identifier == 0:
        operator_function = add
    elif operator_identifier == 1:
        operator_function = multiply
    elif operator_identifier == 2:
        operator_function = devide
    else:
        raise ValueError

    return operator_function
   
def calculate(num_string):
    for character_index in range(len(num_string)):
        value = num_string[character_index]
        if is_a_operator(value):
            operating_function = choose_opereting_function(choose_operator(value))
            return operating_function([calculate(num_string[:character_index]), calculate(num_string[character_index + 1:])])
        elif is_a_number(num_string):
            return float(num_string)

