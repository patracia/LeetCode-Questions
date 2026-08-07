class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        rows = []

        for i in range(numRows):
            rows.append("")

        current_row = 0
        going_down = True

        for ch in s:
            rows[current_row] += ch

            if current_row == numRows - 1:
                going_down = False

            elif current_row == 0:
                going_down = True

            if going_down:
                current_row += 1
            else:
                current_row -= 1

        return "".join(rows)


           
        