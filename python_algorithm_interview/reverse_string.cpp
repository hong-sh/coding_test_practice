#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {

        reverse(s.begin(), s.end());
    }
};

int main()
{
    char c[] = {'h','e','l','l','o'};
    vector<char> *input1 = new vector<char>();
    input1->assign(c, c+5);
    Solution sol;
    sol.reverseString(*input1);
}