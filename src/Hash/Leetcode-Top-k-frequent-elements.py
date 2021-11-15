def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    my_dict = dict()
    for n in nums:
        my_dict[n] =  my_dict.get(n,0)+1 # n
    my_list = [[x,y] for x,y in my_dict.items()] # n
    my_list.sort(key = lambda x: -x[1]) 
    return [x[0] for x in my_list[:k]]


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    for n in nums:
        count[n] =  count.get(n,0)+1

    freq = [[] for _ in range(len(nums)+1)]
    for n,c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:   
            res.append(n)
            if len(res) == k:
                return res