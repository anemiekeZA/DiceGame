
def user_input (prompt, type_=None, min_=None, max_=None, range_=None):
  if min_ is not None and max_ is not None and max_ < min_:
    raise ValueError("Min_ must be less than or equal to max_.")
  while True:
    ui = input(prompt) 
    if type_ is not None:
      try:
        ui = type_(ui)
      except ValueError:
        print("Input must be {0}." .format(type_.__name__)) 
      continue
    if max_ is not None and ui> max_:
      print("Input must be less than or equal to {0}. ".format(max_))    
    elif min_ is not None and ui< min_:
      print("Input must be grater than or equal to {0}". format(min_))
    elif range_ is not None and ui not in range_:
      if isinstance(range_, range):
        template = "input must be betweeen {0.start} and {0.stop}."
        print(template.format(*range_))
      else: 
        template = "Input must be {0}"
        if len(range_) == 1:
          print(template.format(*range_))
        else:
          expected = " or ".join((
            ", ".join(str(x) for x in range_[:-1]),
            str(range_[-1])
          ))
          print(template.format(expected))
    else:
      return ui
