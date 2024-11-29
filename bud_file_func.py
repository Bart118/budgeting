#budgeting read and write functions

#writes a list to a file
def write_list(file, data):
    print("writing the list to a file...")
    text_file = open(file, "w")
    for line in data:
        text_file.write(str(line))
        text_file.write("\n")
    text_file.close()
    print("finished writing")

#reads a text file and returns a list of the results
def read_data(file):
    print("Reading file...")
    result_file = open(file)
    result1 = result_file.readlines()
    result2 = [item.strip() for item in result1]
    return result2
