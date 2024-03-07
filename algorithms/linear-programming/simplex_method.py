from fractions import Fraction

class SimplexMethod:
    def __init__(self, simplex_tableau):
        self.simplex_tableau = [
            list(map(Fraction, row)) for row in simplex_tableau            
        ]

        self.entering_variable_idx = None
        self.pivot_row_idx = None
    
    def run(self):
        while True:
            self._choose_entering_variable()

            if self.entering_variable_idx is None:
                # Optimal solution is found. Stop the algorithm.
                break

            self._choose_pivot_element()

            if self.pivot_row_idx is None:
                # Solution is unbounded. Stop the algorithm.
                break

            self._apply_pivoting_operation()
            self._print_simplex_tableau()

    def _choose_entering_variable(self):
        self.entering_variable_idx = None

        for col_idx in range(1, len(self.simplex_tableau[0]) - 1):
            if self.simplex_tableau[0][col_idx] < 0:
                self.entering_variable_idx = col_idx

    def _choose_pivot_element(self):
        self.pivot_row_idx = None
        min_ratio = float("Inf")

        for row_idx in range(1, len(self.simplex_tableau)):
            ratio = \
                self.simplex_tableau[row_idx][-1] / \
                self.simplex_tableau[row_idx][self.entering_variable_idx]

            if 0 < ratio < min_ratio:
                self.pivot_row_idx = row_idx
                min_ratio = ratio

    def _apply_pivoting_operation(self):
        pivot_element = self.simplex_tableau[self.pivot_row_idx][self.entering_variable_idx]

        for col_idx in range(1, len(self.simplex_tableau[0])):
            self.simplex_tableau[self.pivot_row_idx][col_idx] /= pivot_element
        
        for row_idx in range(len(self.simplex_tableau)):
            if row_idx == self.pivot_row_idx:
                continue

            multiplier = self.simplex_tableau[row_idx][self.entering_variable_idx]

            for col_idx in range(1, len(self.simplex_tableau[0])):
                self.simplex_tableau[row_idx][col_idx] -= \
                    self.simplex_tableau[self.pivot_row_idx][col_idx] * multiplier

    def _print_simplex_tableau(self):
        for row in self.simplex_tableau:
            print(" ".join(list(map(str, row))))
        print()


if __name__ == "__main__":
    simplex_tableau = [
        [1, -13, -23, 0, 0, 0, 0],
        [0, 1, 3, 1, 0, 0, 96],
        [0, 1, 1, 0, 1, 0, 40],
        [0, 7, 4, 0, 0, 1, 238]
    ]

    SimplexMethod(simplex_tableau).run()
