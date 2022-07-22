import math


class Solution:
    def isPalindrome(left: list, right: list) -> bool:
        if len(left) == len(right):
            # check if the positions of the given characters are same on both halves
            # a character from one half can coincide with a "?" on the other side but not a different character
            for i in range(len(left)):
                if left[i] != right[i]:
                    return False
            return True
        return False

    def minimumSum(self, s: str) -> int:
        # divide the string in half
        length = len(s)
        left = s[:length/2]
        # invert one half
        right = s[(length/2)+1:][::-1]
        # check if the string can be made a palindrome
        if isPalindrome(left, right):
            # take the one with most characters
            half = left if left.count("?") < right.count("?") else right
            # replace all "?" with the next character of the adjacent one
            for i in range(length-2):
                if i == 0 and not half[i].isalpha():
                    half[i] = chr(ord(half.lstrip("?")[0])+1)
                elif not half[i].isalpha():
                    half[i] = chr(ord(half[i-1]+1))

            # return the final string by joining the string with it's reverse
            return half+half[::-1]

        return -1


# {
#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.minimumSum(s)

        print(res)


# } Driver Code Ends
