'''

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        /*
        int length=0;
        
        ListNode *point=head, *newhead=head;
        while(point!=NULL){
            length+=1;
            point=point->next;
        }
        if(length==1)
            return NULL;
        int count=length-n-1;
        if(count==-1)
            return head->next;
        while(count){
            count-=1;
            newhead=newhead->next;
        }
        newhead->next=newhead->next->next;
        return head;
        */
        
        if(head==NULL) return head;
        ListNode *first=head,*second=head;
        
        for(int i=0;i<n;i++){
            if(second->next!=NULL) second=second->next;
            else
                return head->next;
        }
        while(second->next!=NULL){
            first=first->next;
            second=second->next;
        }
        first->next=first->next->next;
        return head;
        
    }
};
