#include <iostream>
#include <string>
#include <stack>

using namespace std;
void isMatching(string temp){
    stack<char> string_stack;
    bool unmatched = false;
    int counter =0;
    for (int j =0; j < temp.length(); j++){
            if (temp[j]=='[' || temp[j]=='{' || temp[j]=='<' || temp[j]=='('){
                string_stack.push(temp[j]);
            }else if (temp[j]==']' && !string_stack.empty())
            {
                if (string_stack.top() == '[' ){
                    string_stack.pop();
                } else if (unmatched ==false){
                cout << "NO" << endl;
                unmatched = true;
                break;
            }
            } else if (temp[j]=='}' && !string_stack.empty())
            {
                if (string_stack.top() == '{'){
                    string_stack.pop();
                } else if (unmatched ==false){
                cout << "NO" << endl;
                unmatched = true;
                break;
            }
            } else if (temp[j]=='>' && !string_stack.empty())
            {
                if (string_stack.top() == '<'){
                    string_stack.pop();
                } else if (unmatched ==false){
                cout << "NO" << endl;
                unmatched = true;
                break;
            }
            } else if (temp[j]==')' && !string_stack.empty())
            {
                if (string_stack.top() == '('){
                    string_stack.pop();
                } else if (unmatched ==false){
                cout << "NO" << endl;
                unmatched = true;
                break;
            }
            } else { counter += 1; }
        }
        if(string_stack.empty() && unmatched == false && counter == 0){
                cout << "YES" << endl;
            } else {
                 if (unmatched == false) {
                cout << "NO" << endl;
                 }
            }

}
int main() {
    //Getting the inputs
    string user_input[1000];
    int no_of_lines;

    cin >> no_of_lines;
    for (int i =0; i < no_of_lines; i++){
        cin >> user_input[i];
    }
    //logic
    for (int i =0; i < no_of_lines; i++){
        isMatching(user_input[i]); 
    }

}