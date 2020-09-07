"""

"""
import string

def groupAnagrams(strs: List[str]) -> List[List[str]]:

    alp = { k:v for k,v in zip(string.ascii_lowercase, range(26)) }

    def prep(word):
        stt = [0]*26
        for letter in word:
            h_letter = alp[letter]
            stt[h_letter] += 1
        return tuple(stt)

    bag = {}

    for word in strs:
        key = prep(word)

        if bag.get(key, None):
            bag[key].append(word)
        else:
            bag[key] = [word]

    return bag.values()
