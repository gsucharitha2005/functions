def count_vowels(text):
    count=0
    for i in text:
        if i in "aeiouAEIOU":
            count+=1
    return count

print(count_vowels("Sucharitha"))