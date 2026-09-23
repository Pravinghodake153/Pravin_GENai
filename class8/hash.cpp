#include<iostream>
using namespace std;
int main(){
    hash<string> h;

cout<<h("chirayupravinkeerthikrishnaprasham")<<endl;
cout<<h("num")<<endl;
cout<<h("lol")<<endl;
cout<<h("goal")<<endl;

unordered_map<string,int> mp;

mp["apple"] = 10;
mp["banana"] = 20;
cout << mp["apple"]<<endl;
cout<<mp["banana"];
return 0;
}