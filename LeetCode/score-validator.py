class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score,counter=0,0
        for i in events :
            if i=="W":
                counter+=1
                if counter ==10:
                    return [score,counter]
            elif i=="WD" or i=="NB":
                score+=1
            else:
                score+=int(i)
        return [score,counter]