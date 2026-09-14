class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        st=list(map(int,startTime.split(":")))
        et=list(map(int,endTime.split(":")))
        res=[]
        for i in range(len(st)):
            res.append(et[i]-st[i])
        return res[0]*3600+res[1]*60+res[2]