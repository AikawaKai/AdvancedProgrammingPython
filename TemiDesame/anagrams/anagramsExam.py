words = [word.strip() for word in open('wordlist-anagram.txt')]

def anagrams():
    words = [word.strip() for word in open('wordlist-anagram.txt')]
    max_len = len(sorted(words, key=lambda x: len(x))[-1])
    dict_anagrams = {}
    for w in words:
        stringW = "".join(sorted(w.lower()))
        if stringW in dict_anagrams:
            if w not in dict_anagrams[stringW]:
                dict_anagrams[stringW].append(w)
                dict_anagrams[stringW] = sorted(dict_anagrams[stringW])
        else:
            dict_anagrams[stringW] = [w]
    new_dict = filter(lambda x: len(x[1])>2, dict_anagrams.items())
    new_value = []
    for k, value in sorted(new_dict, key=lambda x: x[1][0]):
        string_ = "{0:15}:- {2}".format(value[0], max_len, ", ".join(value[1:]))
        new_value.append(string_)
    return new_value
if __name__ == '__main__':

    anag = anagrams()
    for value in anag:
        print(value)
