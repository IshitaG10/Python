import pandas as pd

df = pd.read_csv("NATO-alphabet-start\\nato_phonetic_alphabet.csv")

NATO_dictionary = {row.letter:row.code for (index, row) in df.iterrows()}
word = input("Enter a word: ").upper()
word_list = [ch for ch in word]

code_words = [NATO_dictionary[code] for code in word ]

print(code_words)

