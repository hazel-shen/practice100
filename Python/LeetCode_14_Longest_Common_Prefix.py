class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        shortest_string = strs[0]
        
        for i, word in enumerate(strs): # Find out the shortest word
            if i > 0 and len(word) < len(shortest_string):
                shortest_string = word

        same_char = []
        last_index = 0
        result = ""
        for i in range(len(shortest_string)):        
            flag = True
            for word in strs:
                if word[i] != shortest_string[i]:
                    flag = False
                    break
                else:
                    last_index = i

            if flag == False: # Stop comparing
                break

            if flag == True:
                result = ''.join(shortest_string[:last_index + 1])

        return result
                
            
                 
                
        
