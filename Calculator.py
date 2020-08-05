def generate(size):
    output = "def calculate(lh,rh,op):";
    len_ot = len(output) + 2
    operators = ["+","-","*","/"];
    for op in operators:
        for lh in range(size):
            start = 1 if op == "/" else 0;
            for rh in range(start, size):
                output += ("\n\telif ({lh} == lh and \"{op}\" == op and {rh} == rh):\n\t\treturn \"{lh}{op}{rh} = ".format(lh = lh, op = op, rh = rh)+str(eval("{lh}{op}{rh}".format(lh=lh, op=op, rh=rh)))+"\"")
    return output[0: len_ot] + output[len_ot + 2:]
    
    
