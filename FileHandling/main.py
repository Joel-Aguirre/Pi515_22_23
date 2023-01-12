# **********************************************************************************************************************
# Exercise 1
# **********************************************************************************************************************
# Q: Why isn't this code working? How can we change it to read out the entire file?

print("*" * 35)
print("EXERCISE 1")
print("*" * 35 + "\n")

with open("FileHandling/exercise1.txt", "r") as f:
    f_contents = f.read()
    print(f_contents)

print()

# **********************************************************************************************************************
# Exercise 2
# **********************************************************************************************************************

print("*" * 35)
print("EXERCISE 2")
print("*" * 35 + "\n")

f = open("FileHandling/exercise2.txt", "r")

# You can specify the amount of characters read by your code by passing a number through the read() function
# Change your code to print any number of characters (less than 100)
num_of_chars = 34  # TODO: Pick your favorite number 1-100
f_contents = f.read(num_of_chars)  # TODO: Only print out the given number of characters

# Print the characters and end with *
print(f"First {num_of_chars} characters:")
print(f_contents, end="*")

# Use the seek() function to print the first 20 characters
# skip to the 45th character
# print the next 20 characters
print("\n\nCharacters 0-19 and 45-65")
f.seek(0)
f_contents = f.read(20)  # TODO: Replace -1 with correct number
print(f_contents)
f.seek(45)  # TODO: Replace -1 with correct number
f_contents = f.read(20)  # TODO: Replace -1 with correct number
print(f_contents)

f.seek(0)
print()

# Read the entire file into a string
# and print the last 21 characters
f_contents = f.read()
start = len(f_contents) - 21  # TODO: How would we determine the start and finish?
end = len(f_contents)
print(f_contents[start:end])

f.close()

# **********************************************************************************************************************
# Exercise 3
# **********************************************************************************************************************
# Q: Copy exercise3.txt to result.txt line by line in all caps

# Step 1: Read in a line of exercise3.txt
# Step 2: Write the line to result.txt in all caps
# Step 3: Repeat step 1 and 2 for all lines

print("*" * 35)
print("EXERCISE 3")
print("*" * 35 + "\n")

read_file = open("FileHandling/exercise3.txt", "r")
write_file = open("FileHandling/result.txt", "w")
# TODO: Iterate over read file and write to the write file

for line in read_file:
  line = line.upper()
  write_file.write(line)

read_file.close()
write_file.close()
print("Exercise 3 complete.")
