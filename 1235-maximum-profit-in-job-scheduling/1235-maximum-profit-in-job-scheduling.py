class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        # Define BinarySearch function
        def binarySearch(jobs, start):
            lo, hi = 0, len(jobs) - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if jobs[mid][0] <= start:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return hi

        # Create jobs array and sort them based on end times
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])

        # Initialize DP Array
        dp = [(0, 0)]  # (endTime, profit)

        # Iterate and Update DP
        for start, end, prof in jobs:
            i = binarySearch(dp, start)
            if dp[i][1] + prof > dp[-1][1]:
                dp.append((end, dp[i][1] + prof))

        # return the result
        return dp[-1][1]

    ##so sad