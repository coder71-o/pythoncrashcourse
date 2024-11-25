# go through existing to-dos, listing each one asking the user if they completed it
# if they completed it, remove it from the list, if not, keep it on the list

# ask the user to add more todos
# allow the to quit out when they are done adding their todos.

# make sure todos.txt exist
# read todos from todos.txt as a list of strings. Each line should have its own element in the list.

# for loop through the list
    # print the to-dos
    # ask the user if they completed this
        # yes: remove it
        # no: keep it

# while loop
    # ask for another to-do
    # if they input "q"
        # quit out with "break"
    # else
        # add to to-do list

# write new todos to file
try:
    with open("todos.txt", "r") as f:
        content = f.read()
        todo_list = content.split("\n")
except FileNotFoundError:
    with open("todos.txt", "w") as f:
        f.write("")

remaining_todo_list = []

for todo in todo_list:
    print("You have to do:", todo)
    user_input = input("Have you completed this task?(y/n): ")
    if user_input != "y":
        remaining_todo_list.append(todo)

while True:
    new_todo = input("Add todo (q to quit): ")
    if new_todo == "q":
        break
    else:
        remaining_todo_list.append(new_todo)

with open("todos.txt", "w") as f:
    output = "\n".join(remaining_todo_list)
    f.write(output)