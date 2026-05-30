# https://leetcode.com/explore/interview/card/top-interview-questions-easy/
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/math/879/

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

 

# Constraints:

#     1 <= s.length <= 105
#     s[i] is a printable ascii character.

class reversedString():

    def __init__ (self, characters_v: list[str])-> None:
        self.characters: list[str] = characters_v

    def reverseString(self, input_list: list[str]) -> list[str]:
        input_list_length: int = 0
        for i in input_list:
            print(i)
            input_list_length = input_list_length + 1
        
        print("Input list lenght is: "+str(input_list_length))

        new_list: list[str] = [" "] * input_list_length
        
        
        for x in input_list:
             print(x)

             new_list[input_list_length-1]=x

             input_list_length = input_list_length - 1

        
        return new_list
    
rs=reversedString(["h","e","l","l","o"])
print(rs.characters)
print(rs.reverseString(rs.characters))
            


    
