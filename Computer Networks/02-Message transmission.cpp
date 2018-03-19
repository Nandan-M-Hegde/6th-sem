#include <iostream>
#include <vector>
#include <ctime>
#include <algorithm>
#include <limits.h>

using namespace std;

class frames {
public:
    int seq_no;
    string s;
};

vector<frames> split_assign(vector<frames> v, string s, int l) {
    string s1;
    frames f;
    for (int i = 0, j = 0; i < s.length(); i += l, j++) {
        s1 = s.substr(i, l);
        f.seq_no = j;
        f.s = s1;
        v.push_back(f);
    }
    return v;
}

vector<frames> shuffle_frames(vector<frames> v) {
    srand(unsigned(time(NULL)));
    random_shuffle(v.begin(), v.end());
    return v;
}

vector<frames> sort_frames(vector<frames> v) {
    sort(v.begin(), v.end(), [](frames &one, frames &two) { return one.seq_no < two.seq_no; });
    return v;
}

vector<int> get_shortest_path(vector<int> dist, vector<int> parent, int s, int dest, vector<int> path) {
    if (parent[dest] == -1)
        return path;
    path = get_shortest_path(dist, parent, s, parent[dest], path);
    path.push_back(dest);
    return path;
}

int minimum_dist(vector<int> d, vector<bool> spt) {
    int min = INT_MAX;
    int min_index;

    for (int i = 0; i < d.size(); i++) {
        if (spt[i] == false && d[i] <= min) {
            min = d[i];
            min_index = i;
        }
    }
    return min_index;
}

vector<int> find_shortest_path(vector<vector<int>> v, int src, int dest) {
    vector<int> path;
    vector<int> dist;
    vector<bool> spt;
    vector<int> parent;
    for (int j = 0; j < v[0].size(); j++) {
        parent.push_back(-1);
        dist.push_back(INT_MAX);
        spt.push_back(false);
    }
    dist[src] = 0;

    for (int count = 0; count < v[0].size() - 1; count++) {
        int u = minimum_dist(dist, spt);

        spt[u] = true;

        for (int i = 0; i < v[0].size(); i++) {
            if (!spt[i] && v[u][i] && dist[u] + v[u][i] < dist[i]) {
                parent[i] = u;
                dist[i] = dist[u] + v[u][i];
            }
        }
    }
    path = get_shortest_path(dist, parent, src, dest, path);
    return path;
}


int main() {
    int n, src, dest, edges;
    int temp_s, temp_d, temp_len;

    string s;
    int l = 1;
    vector<frames> vec;
    cout << "Enter the message: ";
    getline(cin, s);
    cout << "Enter frame size: ";
    cin >> l;
    vec = split_assign(vec, s, l);
    cout << "Message after splitting and assigning sequence numbers: ";
    for (auto x:vec) {
        cout << x.seq_no << "-" << x.s << endl;
    }
    cout << "Enter the number of nodes: ";
    cin >> n;
    cout << "Enter the source and destination: ";
    cin >> src >> dest;
    if ((src < 0 || src >= n)) {
        src = 0;
    }
    if ((dest < 0 || dest >= n)) {
        dest = 0;
    }
    cout << "Enter the number of edges: ";
    cin >> edges;
    vector<int> temp(n, 0);
    vector<vector<int>> graph(n, temp);
    for (int j = 0; j < edges; j++) {
        cout << "Enter the source node, destination node and length of edge " << j + 1 << ": ";
        cin >> temp_s >> temp_d >> temp_len;
        graph[temp_s][temp_d] = temp_len;
        graph[temp_d][temp_s] = temp_len;
    }

    vector<int> path;
    path = find_shortest_path(graph, src, dest);
    string p = to_string(src);
    for (auto x:path) {
        p += " ";
        p += to_string(x);
    }

    int path_len = path.size();
    cout << path_len << endl;
    cout << "Established path is: " << p << endl;
    int stop_point = rand() % (vec.size() - 1);
    cout << stop_point << endl;
    for (int i = 0; i < stop_point; i++) {
        cout << "Sending frame " << i << " through " << p << endl;
    }

    int rnode1 = rand() % (path_len - 1);
    int rnode2 = rnode1 + 1;
    graph[path[rnode1]][path[rnode2]] = 0;
    graph[path[rnode2]][path[rnode1]] = 0;
    cout << path[rnode1] << " and " << path[rnode2] << " are disconnected\n";
    cout << "New shortest path is established\n";
    path = find_shortest_path(graph, src, dest);

    string p1 = to_string(src);
    for (auto x:path) {
        p1 += " ";
        p1 += to_string(x);
    }
    for (int i = stop_point; i < vec.size(); i++) {
        cout << "Sending frame " << i << " through " << p1 << endl;
    }

    vec = shuffle_frames(vec);
    cout << "Frames are received in the following order\n";
    for (auto x:vec) {
        cout << x.seq_no << "-" << x.s << endl;
    }
    cout << endl;
    vec = sort_frames(vec);
    cout << "After rearranging frames\n";
    for (auto x:vec) {
        cout << x.s;
    }
    cout << endl;
    return 0;
}