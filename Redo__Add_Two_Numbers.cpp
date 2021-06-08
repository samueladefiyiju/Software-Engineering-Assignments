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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
       int carry = 0;
       int sum = 0; 
       ListNode * ans =  new ListNode(0);
       ListNode * answer_head = ans; 
        
        while (l1 != NULL || l2 != NULL){
            if (l1  != NULL){
                 sum += l1->val; 
                 l1 = l1->next; 
           
                
            }
            if (l2 != NULL){
                sum += l2->val;
                l2 = l2->next; 
            }
            sum += carry; 
           
            if (sum >= 10){



                ans->next = new ListNode(sum % 10);
                ans = ans->next; 
                sum = floor(sum/10);
                
            }
            else{
                if (carry > 1){
                ans->next = new ListNode(sum ); 
              
                ans = ans->next;
                carry = 0 ; 
                sum = floor(sum/10);
                }
                else{
                    
                ans->next = new ListNode(sum ); 
                ans= ans->next;
                carry = 0;
                sum = floor(sum/10); 
                
                
                    
                }
          
                
                
            }
         
           
        }
         if (sum > 0){
                ans->next = new ListNode(sum ); 
                ans= ans->next;
            }
        
        return answer_head->next; 

    }
};
