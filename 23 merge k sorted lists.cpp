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
    ListNode* mergeKLists(vector<ListNode*>& lists) 
    {
        auto cmp = [](ListNode* a, ListNode* b) {return a->val > b->val;} ;
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> q(cmp);
        
        // init
        ListNode *head = NULL;
        ListNode *curr;
        for(auto it=lists.begin(); it<lists.end(); it++)
            if(*it)
                q.push(*it);
        if(!q.empty())
        {
            ListNode *a = q.top();
            q.pop();
            head = new ListNode(a->val);
            curr = head;
            if(a->next)
                q.push(a->next);
        }
        while(!q.empty())
        {
            ListNode* a = q.top();
            q.pop();
            curr->next = new ListNode(a->val);
            curr = curr->next;
            if(a->next)
                q.push(a->next);
        }
        return(head);
    }
};
