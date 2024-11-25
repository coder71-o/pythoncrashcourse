# f = open("example.txt", "a")
# f.write("Hello!\nGoodbye!")
# f.close()

# f = open("example.txt", "r")
# content = f.readlines()
# content = [x.strip() for x in content]
# print(content)

# content = f.read()
# print(content.split("\n"))
# f.close()

with open("example.txt", "a") as f:
    f.write("This is the last one! I promise!\n")