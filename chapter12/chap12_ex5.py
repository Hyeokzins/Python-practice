try:
    with open("non_existent_file.txt", "r") as f:
        contents = f.read()

except FileNotFoundError:
    print('FileNotFoundError')