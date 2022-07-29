class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def helper( s ):
            
            # dictionary
            # key   : character
            # value : serial number in string type
            char_index_dict = dict()
            
            # given each unique character a serial number
            for character in s:
                
                if character not in char_index_dict:
                    char_index_dict[character] = str( len(char_index_dict) )
            
            
            # gererate corresponding pattern string
            return ''.join( map(char_index_dict.get, s) )

        #--------------------------------------------------------    
            
        pattern_string = helper(pattern)
        
        return [ word for word in words if helper(word) == pattern_string ]