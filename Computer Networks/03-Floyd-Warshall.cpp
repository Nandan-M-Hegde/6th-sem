#include <vector>
#include <iostream>
using namespace std;

void fw(vector< vector<int> > m) {
    int i,j,k;
    for (k=0; k<m[0].size(); k++) {
        for (i=0; i<m[0].size(); i++) {
            for (j = 0; j<m[0].size(); j++) {
                if ((m[i][k] * m[k][j]) != 0 && (i!=j))
                    if ((m[i][k]+m[k][j] < m[i][j]) || (m[i][j] == 0))
                        m[i][j] = (m[i][k] + m[k][j]);
            }
        }
    }
    for (i=0; i<m[0].size(); i++) {
        cout<<"\n Minimum cost w.r.t node: "<<i<<endl;
        for (j=0; j<m[0].size(); j++) {
            cout<<m[i][j]<<"\t";
        }
    }
}

int main() {
    int n,t;
    cout<<"Enter the number of nodes: ";
    cin>>n;
    vector<int> temp(n,0);
    vector< vector<int>> m(n, temp);
    cout<<"Enter the adjacency matrix\n";
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin>>t;
            m[i][j] = m[j][i] = t;
        }
    }
    fw(m);
    return 0;
}