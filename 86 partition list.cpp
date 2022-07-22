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
    ListNode* partition(ListNode* head, int x)
    {
        ListNode* list0 = NULL;
        ListNode* list1 = NULL;
        ListNode** tail0 = &(list0);
        ListNode** tail1 = &(list1);
        ListNode* thisNode = head;
        while(thisNode)
        {
            if(thisNode->val < x)
            {
                (*tail0) = thisNode;
                tail0 = &(thisNode->next);
            }
            else
            {
                (*tail1) = thisNode;
                tail1 = &(thisNode->next);
            }
            thisNode = thisNode->next;
        }
        (*tail0) = list1;
        (*tail1) = NULL;
        return list0;
    }
};
