class Solution {
public:
    int trap(vector<int>& height) {
        auto left{0};
        while (left < height.size()) {
            if (height[left] > 0) {
                break;
            }
            left++;
        }
        vector<int> post(height.size(), 0);
        auto max{0};
        for (auto i{static_cast<int>(height.size() - 1)}; i >= 0; --i) {
            post[i] = max;
            max = std::max(height[i], max);
        }
        auto ret{0};
        while (true) {
            auto currTrapped{0};
            auto curr{left + 1};
            while (curr < height.size()) {
                if (height[curr] >= height[left]) break;
                if (height[curr] >= post[curr]) break;
                currTrapped += std::min(height[left], post[curr]) - height[curr];
                curr++;
            }
            left = curr;
            if (left == height.size()) {
                break;
            } else {
                ret += currTrapped;
            }
        }
        return ret;
    }
};
