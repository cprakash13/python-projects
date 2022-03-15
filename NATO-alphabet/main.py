import pandas as pd

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pd.read_csv("nato_phonetic_alphabet.csv")
pairs = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("Enter the word: ").upper()
nato_pairs = [pairs[letter] for letter in word]
print(nato_pairs)
