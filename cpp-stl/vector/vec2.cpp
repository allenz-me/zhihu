#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<unordered_set<int>> edges(10);  // 10 个顶点
    edges[1].insert(4);
    edges[1].insert(9);
    vector<unordered_set<int>> edges_copy(edges);
    cout << edges[1].size() << " " << edges_copy[1].size() << endl;  // 2 2
    edges_copy[1].erase(4);
    cout << edges[1].size() << " " << edges_copy[1].size() << endl;  // 2 1
}
