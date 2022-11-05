def generate(size, justAnswer = True):
    if justAnswer: return generate_patterns_just_answer(size);
    else: return generate_patterns(size);
    
    
def generate_patterns(size):
    output = "def calculate(lh,rh,op):\n\tmatch [lh, op, rh]:";
    len_ot = len(output)
    operators = ["+","-","*","/"];
    for op in operators:
        for lh in range(size):
            start = 1 if op == "/" else 0;
            for rh in range(start, size):
                output += ("\n\t\tcase [{lh},\"{op}\",{rh}]:\n\t\t\treturn \"{lh}{op}{rh} = ".format(lh = lh, op = op, rh = rh)+str(eval("{lh}{op}{rh}".format(lh=lh, op=op, rh=rh)))+"\"")
    return output

def generate_patterns_just_answer(size):
    output = "def calculate(lh,rh,op):\n\tmatch [lh, op, rh]:";
    len_ot = len(output)
    operators = ["+","-","*","/"];
    for op in operators:
        for lh in range(size):
            start = 1 if op == "/" else 0;
            for rh in range(start, size):
                output += ("\n\t\tcase [{lh},\"{op}\",{rh}]:\n\t\t\treturn ".format(lh = lh, op = op, rh = rh)+str(eval("{lh}{op}{rh}".format(lh=lh, op=op, rh=rh))))
    return output
    