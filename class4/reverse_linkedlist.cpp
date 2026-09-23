#include<iostream>
using namespace std;
struct Node{
    int data;
    Node* next;
};
Node* reverse(Node* head){
    if(head==NULL){
        return head;
    }
    if(head->next==NULL){
        return head;
    }
    Node* newHead=reverse(head->next);
    head->next->next=head;
    head->next=NULL;
    return newHead;
}

    int main(){
    Node* head=new Node{1,NULL};
    head->next=new Node{2,NULL};
    head->next->next=new Node{3,NULL};
    head->next->next->next=new Node{4,NULL};
    head=reverse(head);
    Node* temp=head;
    while(temp!=NULL){
        cout<<temp->data<<" ";
        temp=temp->next;
    }
    return 0;
}