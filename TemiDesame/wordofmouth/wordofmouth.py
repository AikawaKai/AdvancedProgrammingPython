
words = []
with open("wordlist-7.txt") as file_o:
    for line in file_o:
        words.append(line.strip())
words = sorted(words)
#print(words)
def to_string(list_of_lists):
    if len(list_of_lists)==1:
        return str(list_of_lists[0])
    return str(list_of_lists[0]) + "\n" + to_string(list_of_lists[1:])

def diff1(word1, word2):
    return sum([el[0]!=el[1] for el in zip(word1, word2)]) == 1

def getNear1(word1, tabu):
    return [word for word in words if diff1(word1, word) and word not in tabu]

def recChain(word1, word2, curlist, list_of_lists):
    if word1 == word2:
        list_of_lists.append(curlist)
    return [recChain(word, word2, curlist+[word], list_of_lists) for word in getNear1(word1, curlist)]


def chain(word1, word2):
    list_of_lists = []
    recChain(word1, word2, [word1], list_of_lists)
    list_ = to_string(list_of_lists)
    return list_


if __name__ == '__main__':
  print("### witness → fatness")
  print(chain("witness", "fatness"))
  print("### warning → earring")
  print(chain("warning", "earring"))
  print("### sailing → writing")
  print(chain("sailing", "writing"))
