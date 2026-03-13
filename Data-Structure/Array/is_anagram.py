'''
What is an Anagram ?
An anagram is mean two words or names, both have the same length and each character in each word available
in both way to read but has difference mean.
It looks like reverse but called Anagram when we compare the both to each other match if both sorted.
Example:
word_1 = 'listen'
word_2 = 'silent'
act - cat
post - stop
earth - heart
dusty - study

we have to sort the letter of both words and compare to each other in the same index must match
This is called bottlenect because it has O(NlogN)

overall running time is O(NlogN) + O(N) = O(NlogN)
'''

def isAnagram(word_1, word_2):
    # if the length of the both words are difference it is not anagrams
    if len(word_1) != len(word_2):
        return False
    # sorted both words
    word_1 = sorted(word_1)
    word_2 = sorted(word_2)
    # check each char to each other to make sure is exist
    for x in range(len(word_1)):
        if word_1[x] != word_2[x]:
            return False

    return True

if __name__ == '__main__':
    word_1 = ['t', 'h', 'i', 'n', 'g']
    word_2 = ['n', 'i', 'g', 'h', 't']

    print(isAnagram(word_1, word_2))


