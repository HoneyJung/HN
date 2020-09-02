#include <iostream>
#include<deque>
#define MAX 100+1
using namespace std;

struct shark_info{
	int r;
	int c;
	int s;
	int d;
	int z;
};
int dx[] = { 0, -1, 1, 0, 0 };
int dy[] = { 0, 0, 0, 1, -1 };
deque<deque<deque<int> > > M;
int main()
{
	cout << 3 << endl;
	cout << M[0].size() << endl;
	for(int i=0;i<M.size();i++){
		for(int j=0;j<M[i].size();j++){
			cout << 3 <<endl;
		}
	}
	//cout << M <<endl;
	int R,C,N;
	int r,c,s,d,z;
	deque<shark_info> shark;
	cin >> R >> C >>N;
	cout << N << endl;
	for(int i=0;i<N;i++)
	{
		cin >> r >> c >> s >> d >> z;
		//cout << temp;
		shark.push_back({r,c,s,d,z});
		
	} 
		
}
