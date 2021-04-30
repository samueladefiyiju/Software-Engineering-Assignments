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
    ListNode* deleteDuplicates(ListNode* head) {
        
        std::map<int,int> intMap; 
        ListNode* prev = NULL; 
        
        ListNode* new_head = head; 

        while (head != NULL){
            if (intMap.count(head->val) <= 0){
                intMap[head->val] =1; 
                prev = head; 



                
            }
            else{
                if (head->next == NULL){
                    prev->next = NULL; 
                }
                else{
                    prev->next = prev->next->next; 
                    
                }
                
            }
            
            head = head->next; 
            
            
        }
        
        return new_head; 
        
    }
};
