def alpha_index(alpha, myword):
    letter = sorted(myword, reverse=True, key= lambda x : x.lower())[0]
    lowercase_letter = letter.lower()
    indx = alpha.index(lowercase_letter)
    return str(indx+1) + letter

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(alpha_index(alphabet, "Zebra"))
