class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        heapq.heapify(trainers)
        count=0
        l=0
        players.sort()
        while trainers:
            val=heapq.heappop(trainers)
            if l==len(players):
                break
            if  players[l]<=val:
                count+=1
                l+=1        
        return count