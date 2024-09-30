
## Old way of opening a file
# file_handler = open("save_to.txt", "w")
# file_handler.write("Hello World!!")
# file_handler.close()


## New way of opening a file
with open("save_to.txt", "a") as file_handler:
    file_handler.write("Hello THE NEW World!!\n")