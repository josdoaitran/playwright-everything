import os

# Set system variable from command line:
# export FIRST=3
# export SECOND=3
first = os.environ['FIRST']
print(f"First system variable: ", first)

second = os.environ['SECOND']
print(f"Second system variable: ", second)

print(f"SUM of 2 system variables: ", int(first) + int(second))
