class TwoSum:
    def __init__(self):
        self.check={}
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        self.check[number]=self.check.get(number,0)+1
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        # a pair of number
        for k,c in self.check.items():
            if k!=value-k:#4 2 2
                if (value-k) in self.check:
                    return True
            else:#4 2 2
                if self.check[k]>=2:
                    return True
        return False