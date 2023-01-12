def exponentiate(x, exp):
  """
  Prints the result of x^exp
  """
  try:
    result = x**exp
  # [Optional] Add specific exception handling
  # Add a catch-all exception
  except:
    print("Try again bud.")
  # Add an else clause that prints the result
  else:
    print("You did it!")
    print(result)
  # Add a finally clause
  finally:
    print("Noice")

# Test the function below
exponentiate("Joel",2)