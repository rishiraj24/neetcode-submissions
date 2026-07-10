class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq2 = defaultdict(set)
        freq1 = defaultdict(set)

        for i in range(len(s1)):
            freq1[s1[i]] = 1 + freq1.get(s1[i], 0)

        left = 0

        for r in range(len(s2)):
            freq2[s2[r]] = 1 + freq2.get(s2[r], 0)
            while r-left+1 > len(s1):
                freq2[s2[left]] -= 1
                if freq2[s2[left]] == 0:
                    del freq2[s2[left]]
                left+=1

            if freq2 == freq1:
                return True
        return False