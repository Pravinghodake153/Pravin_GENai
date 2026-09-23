#include <iostream>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main(){
    unordered_map<string,int> m={
        {"apple",4},
        {"banana",12},
        {"orange",3},
        {"dragonfruit",1}
    };

    auto it=find_if(m.begin(),m.end(),[](pair<string,int> p){
        return p.second>5;
    });

    if(it!=m.end())
        cout<<it->first<<" "<<it->second;

    return 0;
}