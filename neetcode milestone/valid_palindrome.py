class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.lower()
        n = len(st)
        i=0
        txt = ""
        def ispali(s:str)->bool:
            pl = s[::-1]
            if pl==s:
                return True
            return False
        while i<n:
            if st[i].isalnum():
                txt+=st[i]
            i+=1
        return ispali(txt)
       
        