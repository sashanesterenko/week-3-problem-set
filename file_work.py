
file_to_read = "referat.txt"
file_to_write = "referat2.txt"

def referat_mod(file_to_read, file_to_write):
    with open(file_to_read, "r", encoding = "utf-8") as file:
    	# cumulative = ""
    	# for current in file:
    	# 	cumulative = " ".join([cumulative, current])
    	# print(cumulative)	
        cumulative = file.read()
    cumulative = str(cumulative)
    splited_cumulative = cumulative.split(" ")
    cumulative_exclamation = cumulative.replace(".", "!")
    referat2_to_file = "\n".join([str(cumulative), "Length of the cumulative string is {} symbols".format(len(cumulative)), "Number of words in the cumulative string is {}".format(len(splited_cumulative)), str(cumulative_exclamation)])
    with open(file_to_write, 'w', encoding = 'utf-8') as second_file:
        second_file.write(referat2_to_file)


if __name__ == "__main__":
    referat_mod(file_to_read, file_to_write)
