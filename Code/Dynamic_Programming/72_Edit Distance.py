class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache=[[float('inf')]*(len(word2)+1) for i in range(len(word1)+1)]
        #row word1
        #col word2
        for j in range(len(word2)+1):
            cache[len(word1)][j]=len(word2)-j
        for i in range(len(word1)+1):
            cache[i][len(word2)]=len(word1)-i
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    #no need to move insert replace delete
                    cache[i][j]=cache[i+1][j+1]
                else:
                    cache[i][j]=1+min(cache[i][j],cache[i+1][j],cache[i][j+1],cache[i+1][j+1])
        print(cache)
        return cache[0][0]