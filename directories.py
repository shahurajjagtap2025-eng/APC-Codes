import os

# Create directory
if not os.path.exists("Data"):
    os.mkdir("Data")

# Check if directory exists
print(os.path.exists("Data"))

# Show current directory
print(os.getcwd())

# Show files and folders
print(os.listdir())

# Rename directory
os.rename("Data", "NewData")

# Change directory
os.chdir("NewData")

# Show current directory
print(os.getcwd())

# Show contents
print(os.listdir())