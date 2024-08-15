class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = {5: 0, 10: 0, 20: 0
        }
        for n in bills:
            notes[n] += 1
            if n == 10:
                if notes[5] < 0:
                    return False
                else:
                    notes[5] -= 1
            if n == 20:
                if notes[10] > 0 and notes[5] > 0:
                    notes[10] -= 1
                    notes[5] -= 1
                elif notes[5] >= 3:
                    notes[5] -= 3
                else:
                    return False

        return True


