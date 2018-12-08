with open("referat.txt", "r", encoding = "utf-8") as file:
	cumulative = ""
	for current in file:
		cumulative = " ".join([cumulative, current])
	print(cumulative)	
cumulative = str(cumulative)
splited_cumulative = cumulative.split(" ")
cumulative_exclamation = cumulative.replace(".", "!")
print(cumulative_exclamation)
referat2_to_file = "\n".join([str(cumulative), "Length of the cumulative string is {} symbols".format(len(cumulative)), "Number of words in the cumulative string is {}".format(len(splited_cumulative)), str(cumulative_exclamation)])
with open('referat2.txt', 'w', encoding = 'utf-8') as second_file:
    second_file.write(referat2_to_file)

