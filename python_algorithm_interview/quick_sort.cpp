#include <vector>


using namespace std;

vector<int> list;

void swap(int left, int right)
{
	int tmp = list[left];
	list[left] = list[right];
	list[right] = tmp;
}

int partition(int low, int high)
{
	int pivot = list[low];
	int left = low+1;
	int right = high;

	while (left < right)
	{
		while (list[left] <= pivot)
			left++;
		while (list[right] > pivot)
			right--;

		if (left < right)
			swap(left, right);
	}
	
	list[low] = list[right];
	list[right] = pivot;
	return right;
}

void quick_sort(int low, int high)
{
	if (low < high)
	{
		int pivot = partition(low, high);
		quick_sort(low, pivot - 1);
		quick_sort(pivot + 1, high);
	}
}

int main() {
	list = { 1, 3, 2, 4, 10, 14, 5, 7, 6 };
	quick_sort(0, list.size() - 1);
}
