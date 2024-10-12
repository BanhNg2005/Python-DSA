class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS, countT = {}, {} # create hashmap

        for i in range(len(s)): # let i iterate through the length of s
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            # countS[s[i]] is the key of the hashmap of the value s at index i
            # everytime we see the same key, we increment the value by 1 or 0 if it doesn't exist
            # ** the get method is for hashmap where it will return the value of the key if it exists
            # or it will just return the default value 
            countT[t[i]] = 1 + countT.get(t[i], 0) # same thing but for t
        for j in countS: # iterate through the hashmap to make sure the values are the same, j is the key
            if countS[j] != countT.get(j, 0): 
                # check if j exists in the T hashmap by using the get method and if the value is the same or not
                return False   
        return True
    # Time complexity: O(n) or O(s + t) since we have to iterate through both of the strings
    # Space complexity: O(1) or O(s + t) because it is up to the size of the s and t strings

    # solution using the Counter module
    # from collections import Counter (import at the top of the file)

    # if len(s) != len(t):
    #     return False
    #
    # s_dict = Counter(s)
    # t_dict = Counter(t)
    #
    # return s_dict == t_dict

    # Time complexity: O(n) because we have to go over all the keys in the s_dict and also check if the keys are the same in the t_dict
    # Space complexity: O(n) because we are storing the frequency of each character in the string s and t


def main() -> None:
    s = 'lmao'
    t = 'maol'
    sol = Solution()
    print(sol.isAnagram(s,t))

if __name__ == '__main__':
    main()