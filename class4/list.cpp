#include<iostream>
using namespace std;
struct Node{
    int data;
    Node* next;
};

bool isCyclic(Node* head){
    Node* slow;
    Node* fast;
    while(fast!=NULL && fast->next!=NULL){
        slow=slow->next;
        fast=fast->next->next;

        if(slow==fast){
            return true;
        }
    }
    return false;
}

int main(){
    Node* head=new Node{1,NULL};
    head->next=new Node{2,NULL};
    head->next->next=new Node{3,NULL};
    head->next->next->next=new Node{4,NULL};

    head->next->next->next->next=head->next;

    if(isCyclic(head)){
        cout<<"true";
    }
    else{
        cout<<"false";
    }
    return 0;
}