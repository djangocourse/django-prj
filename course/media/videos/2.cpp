#include<iostream>

using namespace std;

int main(){
	int n, sum, max;
	int arry[101];
	cin>>n;
	for(int i = 0; i < n; i++)
		cin>>arry[i];
	
	max = 0;
	sum = 0;
	for(int i = 0; i < n; i++){
		sum = 0;
		for(int j = i ; j < n; j++){
			sum += arry[j];
			if (sum > max)
				max = sum;
		}
	}
	cout<<max;
	
	
	
	return 0;
}
