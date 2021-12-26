#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


struct ListNode {
	int val;
	ListNode* next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
	
	ListNode* find_mid(ListNode* list)
	{
		int list_count = 1;
		ListNode* head = list;
		while (head != nullptr)
		{
			head = head->next;
			list_count++;
		}

		head = list;
		for (int i = 0; i < list_count / 2; i++)
		{
			head = head->next;
		}

		return head;
	}

	ListNode* merge(ListNode* left, ListNode* right) {

		ListNode* head = new ListNode();
		ListNode* current = head;
		if (left->val < right->val) {
			current->val = left->val;
			left = left->next;
		}
		else
		{
			current->val = right->val;
			right = right->next;
		}

		while (left != nullptr && right != nullptr)
		{
			if (left->val < right->val)
			{
				current->next = new ListNode(left->val);
				left = left->next;
			}
			else
			{
				current->next = new ListNode(right->val);
				right = right->next;
			}
			current = current->next;
		}

		while (left != nullptr)
		{
			current->next = new ListNode(left->val);
			current = current->next;
			left = left->next;
		}

		while (right != nullptr)
		{
			current->next = new ListNode(right->val);
			current = current->next;
			right = right->next;
		}
		return head;
	}

	ListNode* merge_sort(ListNode* left, ListNode* right) {
		if (right == nullptr)
			return left;

		if (left->next == nullptr && right->next == nullptr)
		{
			return merge(left, right);
		}

		ListNode* left_mid = find_mid(left);
		ListNode* left_head = left;
		while (left_head->next != left_mid)
			left_head = left_head->next;
		left_head->next = nullptr;

		ListNode* right_mid = find_mid(right);
		ListNode* right_head = right;
		while (right_head->next != right_mid)
			right_head = right_head->next;
		right_head->next = nullptr;
		
		ListNode* l1 = merge_sort(left, left_mid);
		ListNode* l2 = merge_sort(right, right_mid);
		return merge(l1, l2);
	}

	ListNode* sortList(ListNode* head) {
		if (head == nullptr || head->next == nullptr) 
			return head;
		ListNode* mid = find_mid(head);
		ListNode* current = head;
		while (current->next != mid)
			current = current->next;
		current->next = nullptr;

		return merge_sort(head, mid);
	}
};

int main()
{
	ListNode* head = new ListNode(3, new ListNode(2, new ListNode(4)));
	Solution sol;
	ListNode* rst = sol.sortList(head);
	while (rst != nullptr) {
		cout << rst->val << endl;
		rst = rst->next;
	}
}
