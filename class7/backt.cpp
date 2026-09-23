#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    string s;
    cin>>s;
    cout<<"\n";

    sort(s.begin(),s.end());

    do{
        cout<<s<<endl;
    }
    
    while(next_permutation(s.begin(),s.end()));
    return 0;
}