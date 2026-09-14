class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # l=0
        # n=len(people)
        # boats=[]
        # r=1
        # while r<n:
        #     w=people[l:r]
        #     if sum(w)>limit:
        #         boats.append(w)
        #         l+=1
        #         r+=1
        #     else:
        #         boats.append(w)
        #         l+=2
        #         r+=2
        # return boats
        people.sort()
        l,r=0,len(people)-1
        boats=0
        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1
            r-=1
            boats+=1
        return boats