class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # arr = []
        # for i in letters:
        #     arr.append(i-'a')
        # p = target - 'a'
        for i in letters:
            if i>target:
                return i
        return letters[0]
