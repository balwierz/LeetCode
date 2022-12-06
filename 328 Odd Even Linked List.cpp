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
    ListNode* oddEvenList(ListNode* head)
    {
        if(head == nullptr || head->next == nullptr)
            return head;
        ListNode* head2 = head->next;
        ListNode* end[2] = {head, head->next};
        ListNode* p = head->next->next;
        int parity = 0;
        while(p != nullptr)
        {
            end[parity]->next = p;
            end[parity] = p;
            p = p->next;
            parity = 1 - parity;
        }
        end[0]->next = head2;
        end[1]->next = nullptr;
        return head;
    }
};
