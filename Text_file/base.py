# -------------------- BASIC COMMANDS --------------------
import os.path

# ---------- Write ----------
"""
       1 => Filename
                2 => Mode
file = open("text.txt", "a")

file.write("Hello World")
l = ["first phrase\n", "second phrase\n", "third phrase\n"]
file.writelines(l)
file.write("\n".join(l))

file.write("\n   End")

file.close()
"""

# ---------- Exercise ----------

file = open('number.txt', 'w')
file.write("Number txt:\n")
for i in range(1, 11):
    file.write(str(i) + '\n')

file.close()


# ---------- Read ----------
"""
file = open('text.txt', 'r')

# text = file.read()

for line in file:
    print(line, end="")
# print(text)

file.close()
"""

# ---------- Error: Missing File ----------
"""
# ----- First method -----
try:
    file = open('textsss.txt', 'r')
except FileNotFoundError:
    print("File not open")
else:
    text = file.read()
    print(text)
    file.close()
# ----- Second method -----

filename = "text.txt"
if os.path.exists('text.txt'):
    print("file exists")
    file = open(filename, 'r')
    text = file.read()
    print(text)
    file.close()
else:
    print("file not exists")
"""

# ---------- Paths, Directory, Deleting ----------

# Manage the construction of file paths in a way that is
# compatible with different OS => No hard paths
filename = os.path.join('rep', 'text.txt')

# if not os.path.exists(filename):
#     os.mkdir("toto")

# os.rmdir("toto")
# os.remove("text.txt")
