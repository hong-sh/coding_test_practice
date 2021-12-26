#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

bool compare1(string s1, string s2)
{
        return s1.substr(0,4) < s2.substr(0,4);
}

bool compare2(string s1, string s2)
{
    return s1.substr(4,s1.length() - 1) < s2.substr(4, s2.length() -1);
}

class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        vector<string> rst;
        vector<string> digit_logs;
        vector<string> letter_logs;
        for(string log : logs)
        {
            if(log.find_first_not_of("dig") == 3)
                digit_logs.push_back(log);
            else
                letter_logs.push_back(log);
        }
        sort(letter_logs.begin(), letter_logs.end(), compare1);
        sort(letter_logs.begin(), letter_logs.end(), compare2);

        rst.insert(rst.end(), letter_logs.begin(), letter_logs.end());
        rst.insert(rst.end(), digit_logs.begin(), digit_logs.end());

        return rst;
    }
};

int main()
{
    const char* args[] = {"dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"};
    vector<string> logs(args, args+5);

    Solution sol;
    vector<string> rst = sol.reorderLogFiles(logs);

    for (string word : rst)
        cout << word << endl;

}