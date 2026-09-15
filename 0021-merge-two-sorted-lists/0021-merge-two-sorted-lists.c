/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode *res = NULL;
    struct ListNode *temp1, *temp2;
    struct ListNode *head;
    temp1 = list1;
    temp2 = list2;
    while (temp1 != NULL && temp2 != NULL) {
        if (temp1 -> val <= temp2 -> val) {
            printf("%d ", temp1 -> val);
            // ListNode *nn = malloc(sizeof(struct ListNode));
            if (res == NULL) {
                res = temp1;
                head = res;
            }
            else {
                res -> next = temp1;
                res = res -> next;
            }
            temp1 = temp1 -> next;
        }
        else {
            printf("%d ", temp2 -> val);
            if (res == NULL) {
                res = temp2;
                head = res;
            }
            else {
                res -> next = temp2;
                res = res -> next;
            }
            temp2 = temp2 -> next;
        }
    }
    while (temp1) {
        if (res == NULL) {
            res = temp1;
            head = res;
        }
        else {
            res -> next = temp1;
            res = res -> next;
        }
        temp1 = temp1 -> next;
    }
    while (temp2) {
        if (res == NULL) {
            res = temp2;
            head = res;
        }
        else {
            res -> next = temp2;
            res = res -> next;
        }
        temp2 = temp2 -> next;
    }
    if (res != NULL) 
        res -> next = NULL;
    return head;
}