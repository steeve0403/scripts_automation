# ---------- Basic Commands ----------
#       1 => Filename
#                 2 => Mode
# file = open("text.txt", "a")
#
# # file.write("Hello World")
# l = ["first phrase\n", "second phrase\n", "third phrase\n"]
# # file.writelines(l)
# file.write("\n".join(l))
#
# file.write("\n   End")
#
# file.close()
# ---------- Exercise ----------

file = open('number.txt', 'w')
file.write("Number txt:\n")
for i in range(11):
    file.write(str(i+1))
    file.write('\n')


