/*
Consecutive Characters
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

*/
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int maxPower(string s) {
        int power = 1;
        int max = 1;
        int prev = s[0];
        for (int i = 1 ; i < s.size(); ++i){
                if (s[i] == prev) {
                    power += 1;
                    if (power > max){
                        max = power ;
                    } 
                    }else {
                        power  = 1;
                        prev = s[i];
                    
                }
            
        }
        return max;
    }
};