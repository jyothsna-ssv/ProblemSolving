class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        survivors = []  # stack to hold asteroids still moving safely

        for rock in asteroids:
            while survivors and rock < 0 < survivors[-1]:
                # one move right, another move left
                top = survivors[-1]

                if abs(rock) > top:
                    # destroys top one
                    survivors.pop()
                    continue
                elif abs(rock) == top:
                    # both
                    survivors.pop()
                break
            else:
                survivors.append(rock)

        return survivors
