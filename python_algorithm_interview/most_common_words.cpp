#include <string>
#include <vector>
#include <algorithm>
#include <regex>
#include <iostream>
#include <sstream>
#include <map>

using namespace std;

class Solution {
public:
    vector<string> split(string input, char delimiter) {
        vector<string> answer;
        stringstream ss(input);
        string temp;

        while (getline(ss, temp, delimiter)) {
            answer.push_back(temp);
        }

        return answer;
    }  

    bool is_banned(string word, vector<string> &banned)
    {
        for(string ban : banned)
        {
            if (!ban.compare(word))
                return true;
        }
        return false;
    }

    bool value_compare(pair<string, int> &m1, pair<string, int> &m2)
    {
        return m1.second < m2.second;
    }

    string mostCommonWord(string paragraph, vector<string>& banned) {
        regex re("[,.!~`@#$%\^&*\(\)-_+=\<\>]");
        paragraph = regex_replace(paragraph, re, "");
        for(int i=0; i<paragraph.length(); i++)
            paragraph[i] = tolower(paragraph[i]);
        vector<string> splited_string = split(paragraph, ' ');
        map<string, int> word_map;
        for(string word : splited_string)
        {
            if(is_banned(word, banned))
                continue;

            if(word_map.find(word) != word_map.end())
                word_map[word]++;
            else
                word_map.insert(pair<string, int>(word, 1));
        }
        
        map<string, int>::iterator iter = word_map.begin();
        pair<string, int> max_key_value(iter->first, iter->second);
        
        while(iter != word_map.end())
        {
            if(max_key_value.second < iter->second)
            {
                max_key_value.first = iter->first;
                max_key_value.second = iter->second;
            }
            iter++;
        }

        return max_key_value.first;
    }
};

int main()
{
    const char* args[] = {"hit"};
    string paragraph("Bob hit a ball, the hit BALL flew far after it was hit.");
    vector<string> banned(args, args+1);
    Solution sol;
    sol.mostCommonWord(paragraph, banned);
}