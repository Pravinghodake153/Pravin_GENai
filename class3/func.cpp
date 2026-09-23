#include <iostream>
using namespace std;

int main(){
    // int n,k;
    // cin>>n>>k;
    
    // auto multiply=[=](int factor){
    //     return [=](int x){
    //         return factor*x;
    //     };
    // };

    // auto add=[=](int factor){
    //     return [=](int x){
    //         return factor+x;
    //     };
    // };
    // auto subtract=[=](int factor){
    //     return [=](int x){
    //         return x-factor;
    //     };
    // };
    // auto multiplyby53=multiply(53);
    // auto addby10=add(10);
    // auto subtractby5=subtract(5);
    // cout<<multiplyby53(10)<<endl;
    // cout<<addby10(10)<<endl;
    // cout<<subtractby5(10)<<endl;
    deque<int> dq;
    dq.push_back(1);
    dq.push_back(2);
    dq.push_back(3);
    dq.push_back(4);
    cout<<dq.back()<<endl;;
    return 0;
}