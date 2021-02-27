#include<iostream>

using namespace std;

int main(){
	long a, b, min, max;
	cin>>a>>b;
	min = a;
	max = b;
	if (a > b){
		min = b;
		max = a;
	}
	
	
	for(long i = 2; i <= max; i++){
		if ( min % i ==  max % i ){
			cout<<i<<' ';
		}
	}
	
	

		


	
	return 0;
}
