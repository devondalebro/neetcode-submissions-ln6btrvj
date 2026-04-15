class Solution {
public:
    struct DSU {
        DSU(int size) {
            parent.resize(size);
            iota(parent.begin(), parent.end(), 0);
            rank.resize(size);
            fill(rank.begin(), rank.end(), 1);
        }
        vector<int> parent{};
        vector<int> rank{};
        int find(int x) {
            if (parent[x] == x) {
                return x;
            }
            return parent[x] = find(parent[x]);
        }
        bool linked(int x, int y) {
            return find(x) == find(y);
        }
        void unite(int x, int y) {
            auto rootX{find(x)};
            auto rootY{find(y)};

            if (rootX == rootY) return;
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootX] = rootY;
                rank[rootX]++;
            }
        }
    };
    int minCostConnectPoints(vector<vector<int>>& points) {
        auto ret{0};
        auto used{0};
        DSU dsu{static_cast<int>(points.size())};
        // create all the edges
        vector<vector<int>> edges{};
        for (auto i{0}; i < points.size(); ++i) {
            for (auto j{i + 1}; j < points.size(); ++j) {
                auto dist{abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])};
                edges.push_back({dist, i, j});
            }
        }
        sort(edges.begin(), edges.end());
        // ascending order
        for (auto i{0}; i < edges.size(); ++i) {
            if (dsu.linked(edges[i][1], edges[i][2])) {
                continue;
            }
            dsu.unite(edges[i][1], edges[i][2]);
            ret += edges[i][0];
            if (++used == points.size() - 1) {
                return ret;
            }
        }
        return ret;
    }
};
