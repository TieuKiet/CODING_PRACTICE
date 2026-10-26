class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for a in asteroids:

            is_destroy = False
            while stack and  (stack[-1] > 0 and a < 0):
                if abs(a) > stack[-1]:
                    stack.pop()

                elif abs(a) == stack[-1]:
                    stack.pop()
                    is_destroy = True
                    break

                elif abs(a) < stack[-1]:
                    is_destroy = True
                    break

            if not is_destroy:
                stack.append(a)

            


        return stack


s = Solution()
print(s.asteroidCollision(asteroids=[10,2,-5]))