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
    ListNode* reverseBetween(ListNode* head, int l, int r)
    {
        if(l == r)
            return head;
        ListNode** oldHeadAddr = &head;
        for(int i=1; i<l; i++)
        {
            oldHeadAddr = &((*oldHeadAddr)->next);
        }
        ListNode* left = (*oldHeadAddr);
        ListNode* right = left->next;
        //cout << "left " << left->val << " right " << right->val << endl;
        for(int i=0; i<r-l; ++i)
        {
            ListNode* rightright = right->next; // can be null
            right->next = left;
            left = right;
            right = rightright; // can be null
        }
        //cout << "left " << left->val << " " << right << endl;
        
        // left is the last inverted node. right is the next node or null
        // oldHeadAddr is a pointer to the pointer to the first inverted node.
        // It must be pointed to "left". While before what it points to pointed to "right".
        (*oldHeadAddr)->next = right;
        *oldHeadAddr = left; 
        return head;
    }
};
