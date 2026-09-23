#include<iostream>
using namespace std;
struct Node{
    int data;
    Node* next;
};

Node* merge(Node* a, Node* b){
    if(a==NULL){
        return b;
    }
    if(b==NULL){
        return a;
    }
    if(a->data<b->data){
       a->next=merge(a->next, b);
       return a;
    }
    else{
        b->next=merge(a,b->next);
        return b;
    }

}



int main(){
    Node* a=new Node{1,NULL};
    a->next=new Node{3,NULL};
    a->next->next=new Node{5,NULL};

    Node* b=new Node{2,NULL};
    b->next=new Node{4,NULL};
    b->next->next=new Node{6,NULL};

    Node* head=merge(a,b);

    cout<<head;
    return 0;
}