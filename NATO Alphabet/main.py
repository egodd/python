import pandas
nato_df = pandas.read_csv('nato_phonetic_alphabet.csv')

dict = {}

# Loop through rows of a data frame
for (index, row) in nato_df.iterrows():
    dict[nato_df.letter.iloc[index]] = nato_df.code.iloc[index]



#TODO 1. Create a dictionary in this format:
# print(dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input('Type your name: \n').upper()
code_list = [dict[letter] for letter in name]
# print(dict.items())
print(code_list)
