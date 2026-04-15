class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trip_set = set()
        nums.sort()
        print(nums)

        for i, n in enumerate(nums):
            print(n)
            if i == len(nums) - 2:
                break
            p1 = i + 1
            p2 = len(nums) - 1
            while p1 < p2:
                sum_p = nums[p1] + nums[p2]
                if sum_p > -n:
                    p2 -= 1 
                elif sum_p < -n:
                    p1 += 1
                else:
                    print("yes")
                    trip_set.add(tuple([n, nums[p1], nums[p2]]))
                    if nums[p1 + 1] == nums[p1]:
                        p1 += 1
                    elif nums[p2 - 1] == nums[p2]:
                        p2 -= 1
                    else:
                        p1 += 1
                        p2 -= 1
        
        trips = []
        for trip in trip_set:
            trips.append(list(trip))
        return trips
                    