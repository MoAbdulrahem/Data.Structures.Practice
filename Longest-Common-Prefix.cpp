/**
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string output;
        output = "";
        char temp;
        int pointer = 0;
        for(int j=0; j<strs[0].size(); ++j){
            if (strs[0]=="")
                break;
            temp = strs[0][pointer];
        for(int i=0; i<strs.size(); ++i){
            
            if (strs[i][pointer] != temp) {
                
                return output;
            }
        }
            output += temp;
            pointer += 1;
            
        }

        return output;
    }
};