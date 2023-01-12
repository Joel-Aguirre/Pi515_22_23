def greet(name):
  try:
    greeting = "Hello " + name + "!"
    print(greeting)
  # Add TypeError handling
  except TypeError:
    print("You did type error")
  # Add a catch-all exception
  except:
    print("You done wrong")

# Test the function below
greet(3)