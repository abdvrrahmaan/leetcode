class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)
        m1, m2 = 10**9 + 7, 10**9 + 9
        b1, b2 = 31, 37
        p1, p2 = [1] * (n + 1), [1] * (n + 1)
        for i in range(1, n + 1):
            p1[i] = p1[i - 1] * b1 % m1
            p2[i] = p2[i - 1] * b2 % m2

        def check(k):
            h1 = h2 = 0
            for i in range(k):
                h1 = (h1 * b1 + nums[i]) % m1
                h2 = (h2 * b2 + nums[i]) % m2

            cnt = {}
            single = 0

            for i in range(n - k + 1):
                if i:
                    h1 = (h1 - nums[i - 1] * p1[k - 1]) % m1
                    h2 = (h2 - nums[i - 1] * p2[k - 1]) % m2
                    h1 = (h1 * b1 + nums[i + k - 1]) % m1
                    h2 = (h2 * b2 + nums[i + k - 1]) % m2

                key = (h1, h2)
                c = cnt.get(key, 0)
                if c == 0:
                    single += 1
                elif c == 1:
                    single -= 1
                cnt[key] = c + 1

            return single > 0

        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l
