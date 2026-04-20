class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // we need an indegree for each course
        // we need to map each course to its neighbours
        // adjacency list
        vector<int> indegree(numCourses, 0);
        vector<vector<int>> adjList(numCourses);
        for (const auto& edge : prerequisites) {
            indegree[edge[0]]++;
            adjList[edge[1]].push_back(edge[0]);
        }
        queue<int> next{};
        for (auto i{0}; i < numCourses; ++i) {
            if (!indegree[i]) next.push(i);
        }
        vector<int> ret{};
        vector<bool> visited(numCourses);
        while (!next.empty()) {
            auto currCourse{next.front()};
            next.pop();
            ret.push_back(currCourse);
            visited[currCourse] = true;
            for (const auto &n : adjList[currCourse]) {
                if (visited[n]) continue;
                if (--indegree[n] == 0) {
                    next.push(n);
                }
            }
        }
        if (ret.size() == numCourses) {
            return ret;
        } else {
            return {};
        }
    }
};
