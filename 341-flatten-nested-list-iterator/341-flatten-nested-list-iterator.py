# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        # Helper function to flatten the nested list 
        def flatten(nl: NestedInteger, flattendList: List):
            for l in nl: # for each object in nested list
                if l.isInteger(): # if the object is integer
                    flattendList.append(l.getInteger())
                else: # if the object is list flatten the list
                    flatten(l.getList(), flattendList)
        
        # Init
        self.flattendList = []
        flatten(nestedList, self.flattendList)  # generate flattend list
        self.n = len(self.flattendList) # get length of the list
        self.idx = 0 # current index
        return
    
    def next(self) -> int:
        val = self.flattendList[self.idx] # get the current element
        self.idx += 1 # increment the index
        return val
    
    def hasNext(self) -> bool:
        return self.idx < self.n # index must be less than the length
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())