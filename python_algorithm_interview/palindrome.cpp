#include <string>
#include <iostream>
#include <regex>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        s = regex_replace(s, regex("[^a-zA-Z]"), "");
        
        for(int i=0; i<s.length(); i++)
            s[i] = tolower(s[i]);

        cout << s << endl;

        int left = 0, right = s.length()-1;
        while(left < right)
        {
            if (s[left] != s[right])
                return false;
            left++; right--;
        }
        return true;
    }
};

int main(void)
{
    string input1 = "A man, a plan, a canal: Panama";
    string input2 = "race a car";
    Solution sol;
    cout << sol.isPalindrome(input1) << endl;
    cout << sol.isPalindrome(input2) << endl;
}