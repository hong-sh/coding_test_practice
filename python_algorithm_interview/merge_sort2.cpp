#include <vector>

using namespace std;

vector<int> list;


void merge(int left, int mid, int right)
{
	int left_start = left;
	int left_end = mid;
	int right_start = mid + 1;
	int right_end = right;

	vector<int> tmp;

	while (left_start <= left_end && right_start <= right_end)
	{
		if (list[left_start] <= list[right_start])
		{
			tmp.push_back(list[left_start]);
			left_start++;
		}
		else 
		{
			tmp.push_back(list[right_start]);
			right_start++;
		}
	}

	while (left_start <= left_end)
	{
		tmp.push_back(list[left_start]);
		left_start++;
	}

	while (right_start <= right_end)
	{
		tmp.push_back(list[right_start]);
		right_start++;
	}

	while (tmp.size() > 0)
	{
		list[right] = tmp.back();
		tmp.pop_back();
		right--;
	}
}

void merge_sort(int left, int right)
{
	if (left < right)
	{
		int mid = (left + right) / 2;
		merge_sort(left, mid);
		merge_sort(mid + 1, right);
		merge(left, mid, right);
	}
}

int main()
{
	list = { 1, 3, 2, 4, 10, 14, 5, 7, 6 };
	merge_sort(0, list.size() - 1);
}
