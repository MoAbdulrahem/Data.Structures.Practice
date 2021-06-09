#include <iostream>
using namespace std;
#define COUNT 10 /////////////////////////////////
// Implementing the binary search tree
class BinarySearchTree{
    private:
        struct Node {  //node
        int value;
        Node* left;
        Node* right;
        };

        Node* root = nullptr; //at first there's no tree
    public:
        void add_new_node(int item){
            Node* new_item = new Node;
            // setting the values of the new node
            new_item->value = item;
            new_item->left = nullptr;
            new_item->right = nullptr;

            if (root == nullptr){ //Tree is empty
                root = new_item; // Set this node as the root
                return;
            }
            //node insertion logic
            Node* temporary = root;
            Node* parent_pointer = nullptr;
            while(temporary != nullptr){
                parent_pointer = temporary; // to keep the value of the last address before temporary becomes nullptr
                if (item <= temporary->value){
                    temporary = temporary->left;
                }else{
                    temporary = temporary->right;
                }

            }

            if (item <= parent_pointer->value){
                parent_pointer->left =new_item;
            } else {
                parent_pointer->right =new_item;
            }
        }
        Node* get_root(){ // a getter for the tree root
            return root;
        }
        int branch_height(Node* temp){
            if(temp == NULL){ // no tree means the height is 0
                return 0;
            }
            int height;
            height = (1 + max(branch_height(temp->left),branch_height(temp->right))); // height = 1+max height of left and right
            return height;
        }
        bool Balanced(Node *root){
            //if the tree is empty then it's a balanced tree
            if (root == nullptr){
                return true;
            }
            // To get height of the left and right sides of the tree
            int left_branch_height = branch_height(root->left);
            int right_branch_height = branch_height(root->right);
            // Checking if the height of the left and right branches make the tree balanced
            if (abs(left_branch_height - right_branch_height) <= 1 && Balanced(root->left) && Balanced(root->right))
            {
                // 2 conditions for a balanced tree
                //      1. Both sub-trees are balanced
                //      2. The height of the two sub-trees differ by **at most** one.
                return true; 
            }

            return false; // if the if conditions were not met then the tree isn't balanced
        } 
};

int main(){
    BinarySearchTree test;
    int no_of_inputs;
    int temp;
    cin >> no_of_inputs;
    for (int i = 0; i < no_of_inputs; i++)
    {
        cin >> temp;
        test.add_new_node(temp);
    }
    if(test.Balanced(test.get_root())){
        cout << "YES";
    } else {
        cout << "NO";
    }
    

    // test.print2D(test.get_root());
}