class Solution {
public:
    ListNode* deleteMiddle(ListNode* head)
    {
        int n = 0;
        for(ListNode* it=head; it != nullptr; it = it->next)
            n++;
        if(n == 1)
            return nullptr;
        int mid = n / 2 - 1;
        ListNode* it;
        for(it=head; mid; mid--, it = it->next)
        {}
        ListNode *tmp = it->next;
        it->next = it->next->next;
        delete tmp;
        return head;
    }
};
