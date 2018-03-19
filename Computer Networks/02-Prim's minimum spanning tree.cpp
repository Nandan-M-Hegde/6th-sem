#include <iostream>
#include <vector>
#include <iomanip>
#include <limits.h>

using namespace std;

void print_mst(vector<int> parent, vector<vector<int> > v) {
    cout<<setw(12)<<"Edge"<<setw(12)<<"Weight"<<endl;
    for(int i=1; i<parent.size(); i++) {
        cout<<setw(10)<<parent[i]<<"-"<<i<<setw(10)<<v[i][parent[i]]<<endl;
    }
}

int min_key(vector<int> key, vector<bool> mst_set) {
    int min = INT_MAX;
    int min_index;
    for (int i=0; i<key.size(); i++) {
        if (mst_set[i] == false && key[i]<min) {
            min = key[i];
            min_index = i;
        }
    }
    return min_index;
}

void prim_mst(vector< vector<int> > v) {
    vector<int> parent;
    vector<int> key;
    vector<bool> mst_set;
    for (int i=0; i<v.size(); i++) {
        parent.push_back(-1);
        key.push_back(INT_MAX);
        mst_set.push_back(false);
    }
    key[0] = 0;
    parent[0] = -1;

    for(int count=0; count<v.size()-1; count++) {
        int u = min_key(key, mst_set);
        mst_set[u] = true;

        for (int i=0; i<v.size(); i++) {
            if (v[u][i] && mst_set[i] == false && v[u][i]<key[i]) {
                parent[i] = u;
                key[i] = v[u][i];
            }
        }
    }
    print_mst(parent, v);
}

int main() {
    int n, x;
    cout<<"Enter the number of edges: ";
    cin>>n;
    vector<int> temp(n, 0);
    vector< vector<int> > vec;
    cout<<"Enter the matrix\n";
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin>>x;
            temp[j] = x;
        }
        vec.push_back(temp);
    }
    prim_mst(vec);
    return 0;
}