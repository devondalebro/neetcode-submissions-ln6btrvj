class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        // two cars a, b become a fleet if aPos < bPos but aTime <= bTime
        vector<pair<int, double>> stuff(position.size());
        for (auto i{0}; i < position.size(); ++i) {
            stuff.emplace_back(pair{position[i], (target - position[i]) / static_cast<double>(speed[i])});
        }
        std::sort(stuff.begin(), stuff.end(), greater<pair<int, double>>());
        auto prevTime{0.0};
        auto fleets{0};
        for (const auto &[_, time] : stuff) {
            if (time > prevTime) {
                fleets++;
                prevTime = time;
            } 
        }
        return fleets;
    }
};
