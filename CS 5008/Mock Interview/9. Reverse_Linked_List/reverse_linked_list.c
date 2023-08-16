/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// time complexity = O(n)
// space complexity = O(n)


// Define a function to check if the stack is full
int isfull(struct ListNode *t)
{
    struct ListNode *q=(struct ListNode *)malloc(sizeof(struct ListNode));
    if(q==NULL)
    {
        return 1;
    }
    else
    return 0;
}

// Define a function to check if the stack is empty
int isempty(struct ListNode *t)
{
    if(t==NULL)
    {
        return 1;
    }
    else
    return 0;
}

// Define a function to push a node to the stack
struct ListNode *push(struct ListNode *t,int val)
{
    // Check if the stack is full
    if(isfull(t))
    printf("stack full");
    else
    {
        // Create a new node
        struct ListNode *q=(struct ListNode *)malloc(sizeof(struct ListNode));
        q->val=val;

        // Add the node to the stack
        q->next=t;
        t=q;
        return t;
    }
    return t;
}

// Define a function to reverse the linked list
struct ListNode* reverseList(struct ListNode* head){
    struct ListNode *u=head;
    struct ListNode *top=NULL;
    while(u!=NULL)
    {
        top=push(top,u->val);
        u=u->next;
    }
    return top;

}