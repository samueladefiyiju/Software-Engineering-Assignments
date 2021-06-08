/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == NULL || headB == NULL){
            return NULL; 
        }
        
        ListNode* headofA = headA;  
        ListNode* headofB = headB; 
        while(headofA != headofB){
        
            if(headofA == NULL){
                    headofA = headB ;
                }
            else{
                headofA = headofA->next; 
            }
            if(headofB == NULL){
                headofB = headA; 
               
            }
            else{
                headofB = headofB->next; 
            }
            
            }
        
        
        return headofA; 
        
    }
};
