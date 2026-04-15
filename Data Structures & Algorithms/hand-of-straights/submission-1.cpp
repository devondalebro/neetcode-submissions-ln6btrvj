class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if (hand.size() % groupSize != 0) return false;
        std::sort(hand.begin(), hand.end());
        auto hands{hand.size() / groupSize};
        vector<std::pair<int, int>> groups(hands, std::pair(-1, -1));
        for (const auto &h : hand) {
            auto found{false};
            for (auto &g : groups) {
                if (g.first == -1) {
                    g.first = h;
                    g.second = h + groupSize - 1;
                    found = true;
                    break;
                } else if (g.first == h - 1 && g.first != g.second) {
                    g.first = h;
                    found = true;
                    break;
                } 
            }

            if (!found) {
                return false;
            }
        }
        return true;
    }
};
