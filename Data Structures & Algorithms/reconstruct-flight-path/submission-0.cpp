class Solution {
public:
    bool sol(vector<string>& res, const string &curr, int total, unordered_map<string, vector<string>>& adj) {
        res.push_back(curr);
        if (res.size() == total) return true;
        for (auto &dest : adj[curr]) {
            if (dest == "") continue;
            auto d{dest};
            dest = "";
            if (sol(res, d, total, adj)) return true;
            dest = d;
        }
        res.pop_back();
        return false;
    }

    vector<string> findItinerary(vector<vector<string>>& tickets) {
        sort(tickets.begin(), tickets.end());
        unordered_map<string, vector<string>> adj{};
        for (const auto &t : tickets) {
            adj[t[0]].push_back(t[1]);
        }
        vector<string> res{};
        sol(res, "JFK", tickets.size() + 1, adj);
        return res;
    }
};
