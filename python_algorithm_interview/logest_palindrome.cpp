#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool is_palindrome(string s)
    {
        string::iterator iter = s.begin();
        string::iterator reverse_iter = s.end()-1;
        while(iter < reverse_iter)
        {
            if ((*iter) != (*reverse_iter))
                return false;
            iter++; reverse_iter--;
        }
        return true;
    }

    string longestPalindrome(string s) {
        for(int i=s.length(); i > 0; i--)
        {
            int left = 0;
            while(left + i <= s.length())
            {
                string tmp(s, left, i);
                if(is_palindrome(tmp))
                    return tmp;
                left++;
            }
        }
    }
};

int main()
{
    string input1 = "babad";
    string input2 = "cbbd";
    string input3 = "abccccdd";
    Solution sol;
    cout << sol.longestPalindrome(input3) << endl;
}