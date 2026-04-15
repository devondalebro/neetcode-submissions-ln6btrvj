class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        sort(numbers.begin(), numbers.end());
        auto lo{0};
        auto hi{numbers.size() - 1};
        while (numbers[lo] + numbers[hi] != target) {
            if (numbers[lo] + numbers[hi] < target) {
                lo++;
            } else {
                hi--;
            }
        }
        return {lo + 1, hi + 1};
    }
};
