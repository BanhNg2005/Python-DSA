class Solution:
    def mergeStringAlternatively(self, word1: str, word2: str) -> str:
        A, B = len(word1), len(word2)
        a, b = 0, 0 # starts from the first letter
        s = [] # create an empty list because of its efficiency

        word = 1 # word1 is 1 and word2 is 2
        while a < A and b < B:
            if word == 1:
                s.append(word1[a]) # s appends the letter of word1 at its index a
                a += 1 # increment a
                word = 2 # switch to word2
            else:
                s.append(word2[b]) # s appends the letter of word2 at its index b
                b += 1 # increment b
                word = 1 # switch to word1

        # create another 2 while loops to catch any remaining letters in either word1 or word2
        while a < A:
            s.append(word1[a])
            a += 1

        while b < B:
            s.append(word2[b])
            b += 1

        return ''.join(s) # join the list of s into the empty string
        # Time: O(A + B) where A is the length of word1 and B is the length of word2
        # Space: O(A + B)

# Test case
def main() -> None:
    word1 = 'ab'
    word2 = 'pqrs'
    sol = Solution()
    print(sol.mergeStringAlternatively(word1, word2))

if __name__ == '__main__':
    main()


