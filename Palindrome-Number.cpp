class Solution {
public:
    bool isPalindrome(int x) {
        // My first Trash Solution
//         std::queue<int> s;
//         int original = x;
//         int size = 0;
//         if (x < 0){
//             return false;
//         } else {
//             int temp;
//             while(x!= 0) {
//                 temp = x%10;    
//                 s.push(temp);
//                 size += 1;
//                 x = (x-temp)/10;
//                 // std::cout<<s.front()<<std::endl;
//             }
//         }
        
//         int new_int = 0;
//         long long multiplier = pow(10,size-1);
//         // multiplier = 10**(multiplier);
//         while (!s.empty()){
//             new_int += s.front()*multiplier;
//             multiplier /= 10;
//             s.pop();
//         }
//         // std::cout << "int: "<< new_int;
//         if(new_int == original){
//             return true;
//         }else
//             return false;
//     }
        // Second better solution:
        if (x<0)
            return false;
        int base = 1;
        while (x/base >= 10){
            base *=10;
        }
        while (x>0){
            int right = x%10;
            int left = x/base;
            if (right != left){
                return false;
            }
            else {
                x=(x%base)*0.1;
                base *= 0.01;
            }
        }
        return true;
    }
        
        
    
};