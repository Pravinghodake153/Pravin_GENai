#include<iostream>
#include<deque>
using namespace std;
int main(){
    deque<int>d={10,20,30};
    auto addfront=[&](int x){
        d.push_front(x);
    };
    auto addback=[&](int x){
        d.push_back(x);
    };
    auto removefront=[&](){
        d.pop_front();
    };
    addfront(5);
    addback(40);
    removefront();

    for(int x:d){
        cout<<x<<" ";
    }

    return 0;
}