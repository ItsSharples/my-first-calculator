def generate(size, justAnswer = True):
    output = "def calculate(lh,rh,op):\n\tmatch [lh, op, rh]:";
    operators = ["+","-","*","/"];
    for op in operators:
        for lh in range(size + 1):
            start = 1 if op == "/" else 0;
            for rh in range(start, size + 1):
                output += "\n\t\tcase [{lh},\"{op}\",{rh}]:\n\t\t\treturn ".format(lh = lh, op = op, rh = rh)
                if justAnswer:
                    output += str(eval("{lh}{op}{rh}".format(lh=lh, op=op, rh=rh)))
                else:
                    output += "\"{lh}{op}{rh} = ".format(lh = lh, op = op, rh = rh)+str(eval("{lh}{op}{rh}".format(lh=lh, op=op, rh=rh)))+"\""
    return output