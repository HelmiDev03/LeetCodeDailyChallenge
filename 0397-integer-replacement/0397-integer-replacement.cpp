class Solution {
public:
    int integerReplacement(long n) {
       
        if (n==1){
            return 0;
        }
        else if (n==2){
        return 1;}
        else if (n%2==0){
            return 1+ integerReplacement(n/2);
        }
        else {
            return 1 + min( integerReplacement(n+1), integerReplacement(n-1));
        }

        
    }
    /* tawa wehel fi zok om ekher adad 2147483647 */
};