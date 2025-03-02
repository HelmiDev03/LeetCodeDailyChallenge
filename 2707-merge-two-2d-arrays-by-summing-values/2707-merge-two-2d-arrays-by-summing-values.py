class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res=nums1+nums2
        res.sort(key=lambda x:x[0])
        dic={}
        for i in res:
            if i[0] in dic:
                dic[i[0]]+=1
            else:
                dic[i[0]]=1
        final=[]
        i=0
        j=1
        while i<len(res):
            if dic[res[i][0]]>1:
                final.append([res[i][0],res[i][1]+res[j][1]])
                i+=2
                j+=2
            else:
                final.append(res[i])
                i+=1
                j+=1
        return final
        