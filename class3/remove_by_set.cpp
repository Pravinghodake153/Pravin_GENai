#include<iostream>
#include<vector>
#include<set>
using namespace std;

int main(){
    vector<int>v={4,2,4,1,2,3,1};
    set<int>s;
    for(int x:v){
        s.insert(x);
    }
    for(int x:s){
        cout<<x<<" ";
    }
    return 0;
}