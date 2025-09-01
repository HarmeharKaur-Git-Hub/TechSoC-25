# Decrypt Caesar cipher text with a given shift
def decoder(x,z):
    # shift the ASCII values of alphabets
    list3=[]
    for i in list2:
    #for capital letters
        if i in range(65,91):
            if i in range( 65+z,91):
                j=i-z
            else:
            #i=64+z-(90-j)
                j=i-z+26
    #for small letters
        elif i in range(97,123):
            if i in range(97+z,123):
                j=i-z
            else:
            #i=96+z-(122-j)
                j=i-z+26
    #for anything other than letters
        else:
            j=i
        list3.append(j)
    #convert new ASCII values to their respective characters
    list4=[]
    for m in list3:
        list4.append(chr(m))
    #convert the list of new charcters to a string
    y=''.join(list4)
    return y
# Count letter frequencies in a string
def get_letter_frequencies(y):
    total_letters = 0
    counts = {}
    for letter in english_frequency:
        counts[letter] = 0  # initialize with 0

    for char in y:
        if char.isalpha():
            c = char.upper()
            counts[c] += 1
            total_letters += 1

    freqs = {}
    if total_letters == 0:
        for letter in counts:
            freqs[letter] = 0
    else:
        for letter in counts:
            freqs[letter] = (counts[letter] / total_letters) * 100
    return freqs
# Calculate Chi-squared score
def chi_squared(freqs):
    chi = 0
    for letter in freqs:
        expected =english_frequency[letter]
        actual = freqs[letter]
        chi += ((actual - expected) ** 2) / expected
    return chi

english_frequency= {
    'A': 8.2, 'B': 1.5, 'C': 2.8, 'D': 4.3, 'E': 12.7, 'F': 2.2,
    'G': 2.0, 'H': 6.1, 'I': 7.0, 'J': 0.15, 'K': 0.8, 'L': 4.0,
    'M': 2.4, 'N': 6.7, 'O': 7.5, 'P': 1.9, 'Q': 0.10, 'R': 6.0,
    'S': 6.3, 'T': 9.1, 'U': 2.8, 'V': 1.0, 'W': 2.4, 'X': 0.15,
    'Y': 2.0, 'Z': 0.07
}
x=input("Enter the message:")
#convert string into a list of characters
list1=list(x)
# make a list of their ASCII values
list2=[]
for n in list1:
    list2.append(ord(n))
lowest_score=None
best_shift=0
for a in range(0,26):
    z=a
    y=decoder(x,z)
    freqs=get_letter_frequencies(y)
    score=chi_squared(freqs)
    if lowest_score is None or score < lowest_score:
        lowest_score=score
        best_shift =a
decoded_message=decoder(x,best_shift)
print("The best shift value is",best_shift)
print("The decoded message is :")
print(decoded_message)
