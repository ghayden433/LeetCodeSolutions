class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def val():
            return 0
        s1Map = defaultdict(val)
        s2Map = defaultdict(val)

        def check(map1, map2):
            for key in map1.keys():
                if map1[key] != map2[key]:
                    return False
            return True

        for letter in s1:
            s1Map[letter] = s1Map[letter] + 1

        l = 0
        r = 0
        while (r < len(s2)):
            if r < len(s1):
                s2Map[s2[r]] = s2Map[s2[r]] + 1
                r += 1
            else:
                print(l, r)
                s2Map[s2[l]] = s2Map[s2[l]] - 1
                l += 1
                s2Map[s2[r]] = s2Map[s2[r]] + 1
                r += 1
            if (check(s1Map, s2Map)):
               return True

        return False 

        