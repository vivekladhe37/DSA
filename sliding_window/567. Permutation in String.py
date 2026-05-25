class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        cs1 = [0] * 26
        cs2 = [0] * 26

        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        for i in range(n1):
            cs1[ord(s1[i]) - 97] += 1
            cs2[ord(s2[i]) - 97] += 1
        
        if cs1 == cs2:
            return True
        
        for i in range(n1, n2):
            cs2[ord(s2[i]) - 97] += 1
            cs2[ord(s2[i - n1]) - 97] -= 1
            if cs2 == cs1:
                return True

        return False


        