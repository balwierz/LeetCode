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
    ListNode* reverseKGroup(ListNode* head, int k)
    {
        // precalculate the length of the list so that we dont reverse part of k in the end
        int n = 0;
        ListNode* curr = head;
        while(curr)
        {
            n++;
            curr = curr->next;
        }
        ListNode** oldHeadAddr = &head;
        ListNode* ans = head;  // in case no exchange happens
        for(int loop=0; loop<n/k; loop++)
        {
            ListNode* left = *oldHeadAddr;
            ListNode* right = left->next;
            //cout << "Loop " << loop << " left=" << left->val << " right=" << right->val <<  
            //    " oldHeadAddr=" << (*oldHeadAddr)->val << endl;
            for(int i=1; i<k; i++)  // count from 1 because there are k-1 internal reorientations
            {
                //cout << "i=" << i << endl;
                ListNode* rightright = right->next;
                right->next = left;
                left = right;
                right = rightright;
            }
            //cout << "left=" << left->val << " right=" << right->val <<  endl
            ListNode* first = (*oldHeadAddr);
            first->next = right;
            
            if(loop==0)
                ans = left;
            else
                (*oldHeadAddr) = left;
            
            oldHeadAddr = &(first->next);
            
            /*curr = ans;
            while(curr)
            {
                //cout << curr->val << " " << flush;
                curr = curr->next;
            }*/
        }
        return ans;        
    }
};
