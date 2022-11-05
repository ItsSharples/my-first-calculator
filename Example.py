import Calculator

output = Calculator.generate(100)

with open("Output.py", mode = "w") as file:
  file.write(output)
  
import Output
 
assert Output.calculate(10,10,"+") == 20, "The Generator is Borked oops"
