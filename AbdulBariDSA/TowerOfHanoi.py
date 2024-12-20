class Solution:
    def TOH(self, n, a, b, c):
        # recursive method
        # logic: move n-1 disks from A to B using C as auxiliary
        # then move the last disk from A to C
        # then move n-1 disks from B to C using A as auxiliary
        if n > 0:
            self.TOH(n - 1, a, c, b)
            print(f"Move disk {n} from {a} to {c}")
            self.TOH(n - 1, b, a, c)

def main() -> None:
    n = 5
    a = "A"
    b = "B"
    c = "C"
    sol = Solution()
    sol.TOH(n, a, b, c)

if __name__ == '__main__':
    main()