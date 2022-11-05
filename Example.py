import Calculator

output_true = Calculator.generate(100, True)
output_false = Calculator.generate(100, False)
with open("JustAnswers.py", mode = "w") as file:
  file.write(output_true)
with open("Equations.py", mode = "w") as file:
  file.write(output_false)

import JustAnswers, Equations
assert JustAnswers.calculate(10,10,"+") == 20, "The Generator is Borked oops"
assert Equations.calculate(10,10,"+") == "10+10 = 20", "The Generator is Borked oops"
