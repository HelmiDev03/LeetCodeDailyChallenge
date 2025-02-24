class Solution {
public:
    int mod(int n, int k)
    {
        int ans = n % k;
        if(n < 0) ans += k;
        return ans;
    }
	int peopleAwareOfSecret(int n, int delay, int forget) {
        vector<int>arr(n+1);
        arr[1] = 1;
        int knows = 0;  //number of new people got to know the secret from others
		
		//directly starting with the day at which person A start disclosing the secret
        for(int i=delay+1; i<=n; ++i) {
			//update number of people who know the secret
            if(i > forget) knows -= arr[i-forget]; 
            knows += arr[i-delay];
			
            knows = mod(knows, 1000000007);
            arr[i] = knows;
        }
        int sum = 0;
		//sum of all the people who knows the secret, 
		// from the day after which no one will forget the secret 
		// i.e. (n-forget+1)th day
        for(int i=n-forget+1; i<=n; ++i) sum = (sum + arr[i])%1000000007;
        return sum;
    }
};