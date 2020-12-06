class Seat:
    def __init__(self, binary_code):
        row_codes = [c == 'F' for c in binary_code[:7]]
        column_codes = [c == 'L' for c in binary_code[7:]]
        self.row = Seat.translate(row_codes)
        self.column = Seat.translate(column_codes)
        self.id = self.row * 8 + self.column

    @staticmethod
    def translate(codes):
        """Identifies number halving based on """
        count = len(codes)
        rows = range(2**count)
        binaries = [2**x for x in range(count)][::-1]
        sets = zip(codes, binaries)
        for code, binary in sets:
            rows = rows[:binary] if code else rows[binary:]
        return list(rows)[0]