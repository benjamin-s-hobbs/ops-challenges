import os

# === All about os.walk ===
# In os.walk, root prints out directories only from what you specified
# In os.walk, dirs prints out sub-directories from root
# In os.walk, files prints out all files from root and directories

### Read user input here into a variable

### Declare a function here

for (root, dirs, files) in os.walk("testdir"):
    ### Add a print command here to print ==root==
    print(root)
    ### Add a print command here to print ==dirs==
    print(dirs)
    ### Add a print command here to print ==files==
    print(files)

# Main

### Pass the variable into the function here

# End