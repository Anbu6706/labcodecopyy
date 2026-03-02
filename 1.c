#include <stdio.h>
#include <stdlib.h>
struct node{
        int data;
        struct node *next;
    };
struct node*create(){
    struct node *head = NULL, *newnode = NULL, *temp = NULL;
    int choice = 1;
    while (choice == 1){
        newnode = (struct node*)malloc(sizeof(struct node));
        printf("Enter the data : ");
        scanf("%d", &newnode->data);
        newnode->next = NULL;
        if (head == NULL){
            head = newnode;
            temp = head;
        }
        else
        {
            temp->next = newnode;
            temp = temp->next;
        }
        printf("Press 1 to continue or 0 to stop");
        scanf("%d", &choice);
    }
    return head;
}

void display(struct node* head)
{ 
    struct node *temp=NULL;
    temp=head;
    while(temp!=NULL)
    {
        printf("%d->",temp->data);
        temp=temp->next;
    }
    printf("NULL\n");

}

int main()
{
    struct node *head=NULL;
    head=create();
    display(head);   
    return 0;
}