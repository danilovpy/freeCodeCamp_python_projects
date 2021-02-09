def tests(problems):
  problems = [x.split() for x in problems]
  if len(problems) > 5:
    return 'Error: Too many problems.'
  for item in problems:
    try:
      if item[1] != "+" and item[1] != "-":
        return "Error: Operator must be '+' or '-'."
      if len(item[0]) > 4  or len(item[2]) > 4:
        return 'Error: Numbers cannot be more than four digits.'
      int(item[0])
      int(item[2])
    except ValueError:
      return 'Error: Numbers must only contain digits.'
  return problems



#I could've looped over strings and slice instead of splitting.
def arithmetic_arranger(problems, count_bool=False):
  test = tests(problems)
  if type(test) == str:
    return test
  else:
    problems = test
  spaces = 0
  side_spaces = "    "
  result = ""
  loop_count = 7 if count_bool == True else 5
  for i in range(0,loop_count,2):
    for item in problems:
      spaces = len(item[0])+2 if len(item[0])>len(item[2]) else len(item[2])+2
      if i == 6:
        if count_bool == True:
          number = eval("".join(item))
          num = spaces - len(str(number))
          result += " "*num+str(number) +side_spaces
      elif i == 0:
        num = spaces - len(item[i])
        result += " "*num + item[i] + side_spaces
      elif i==2:
        num = spaces - len(item[i]) - 1
        result += item[1]+" "*num + item[i] + side_spaces
      elif i == 4:
        result += "-"*spaces + side_spaces
      if item == problems[-1]:
        result = result.rstrip()
    result += "\n"

  return result.rstrip("\n")

