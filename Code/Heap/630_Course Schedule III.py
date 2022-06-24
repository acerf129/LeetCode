class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:[x[1]])
        time,count=0,0

        for i in range(len(courses)):
            if time+courses[i][0]<=courses[i][1]:
                time+=courses[i][0]
                count+=1
            else:
                maxi=i
                for j in range(i):
                    if courses[j][0]>courses[maxi][0] :
                        maxi=j
                if courses[maxi][0]>courses[i][0]:
                    time=time+courses[i][0]-courses[maxi][0]
                courses[maxi][0]=-1
        return count

        courses.sort(key=lambda x:[x[1]])
        time,count=0,0
        maxHeap=[]
        for c in courses:
            if time+c[0]<=c[1]:
                heapq.heappush(maxHeap,-c[0])
                time+=c[0]
            elif len(maxHeap)>0 and -maxHeap[0]>c[0]:
                time+=heapq.heappop(maxHeap)+c[0]
                heapq.heappush(maxHeap,-c[0])
        return len(maxHeap)