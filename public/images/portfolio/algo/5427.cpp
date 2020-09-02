#include<cstdio>
#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<utility>
#include<deque>
#define MAX 1005
#define INF 0x7fffffff
using namespace std;
int visited[MAX][MAX];
char M[MAX][MAX];
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};
int testcase,m,n,i,j;
typedef struct tuple{
	int i;
	int j;
	int depth;
}tuple;
tuple temp,mecur,firecur;
deque <tuple> fire;
deque <tuple> me;
deque <tuple> ::iterator iter;
int main(){
	scanf("%d",&testcase);

	while (testcase--)
	{
		fire.clear();
		me.clear();
		scanf("%d %d",&m,&n);
		///////////////////////////////////////////////////// 배열 입력 받기 및 visited 초기화. 
		for(i=0;i<n;i++)
		{
			getchar();
			fill_n(visited[i],m,0);
			for(j=0;j<m;j++)
			{
				scanf("%c",&M[i][j]);
				tuple temp = {i,j,0};
				if(M[i][j] == '*')
				{
					fire.push_back(temp);
				}
				if(M[i][j] == '@')
				{
					me.push_back(temp);
					visited[i][j] = 1;
					M[i][j] = '.';
				}
				
			}
		}
		for(i=0;i<n;i++)
				{
					for(j=0;j<m;j++)
					{
						printf("(%d,%d)%c ",i,j,M[i][j]);
					}
					printf("\n");
				}
		/////////////////////////////////////////////////////////////////////////////////
		int flag = 0;
		while(!me.empty())
		{
			if(flag == 1)
			{
				break;
			}
			int before = -1;
			while(!me.empty())
			{
				for(iter=me.begin();iter != me.end();iter++) ////////////////////////////////////me 출력 
				{
					printf("(%d %d %d) ",(*iter).i,(*iter).j,(*iter).depth);
				}
				printf("\n");
				tuple mecur = me.front();
				me.pop_front();
				//////////////////////////////////////////
				printf("%d %d,%d %d\n",mecur.i,mecur.j,mecur.depth,before);          
				//////////////////////////////////////////
				if(mecur.depth != before)
				{
					me.push_front(mecur);
					break;
				}
				before = mecur.depth;
				for(i=0;i<4;i++)
				{	
					tuple temp = {mecur.i+dx[i],mecur.j+dy[i],mecur.depth+1};
					flag = 0;
					if(mecur.i+dx[i] >= n || mecur.i + dx[i] < 0 || mecur.j+dy[i] < 0 || mecur.j+dy[i] >= m)
					{
						flag = 1;
						break;
					}
					if(M[mecur.i+dx[i]][mecur.j+dy[i]] == '#' || M[mecur.i+dx[i]][mecur.j+dy[i]] =='*' || visited[mecur.i+dx[i]][mecur.j+dy[i]] == 1)
					{
						continue;
					}
					visited[mecur.i+dx[i]][mecur.j+dy[i]] = 1;
					me.push_back(temp);
				}
				if(flag == 1)
				{
					break;
				}
			}
			if(flag == 1)
			{
				printf("%d\n",mecur.depth);
			}
			if(me.empty())
			{
				for(i=0;i<n;i++)
				{
					for(j=0;j<m;j++)
					{
						printf("%c ",M[i][j]);
					}
					printf("\n");
				}
				printf("IMPOSSIBLE\n");
				break;
			}
			before = -1 ;
			while(!fire.empty())
			{
				tuple firecur = fire.front();
				fire.pop_front();
				if(firecur.depth == before)
				{
					fire.push_back(firecur);
					break;
				}
				before = firecur.depth;
				for(i=0;i<4;i++)
				{
					tuple temp = {firecur.i+dx[i],firecur.j+dy[i],firecur.depth+1};
					if(firecur.i+dx[i] >= n || firecur.i + dx[i] < 0 || firecur.j+dy[i] < 0 || firecur.j+dy[i] >= m)
					{
						continue;
					}
					if(M[firecur.i+dx[i]][firecur.j+dy[i]] == '#' || M[firecur.i+dx[i]][firecur.j+dy[i]] == '*' )
					{
						continue;
					}
					fire.push_back(firecur);
					M[firecur.i+dx[i]][firecur.j+dy[i]] = '*';
				}
			}
			for(i=0;i<n;i++)
			{
				for(j=0;j<m;j++)
				{
					printf("%c ",M[i][j]);
				}
				printf("\n");
			}
			for(iter=fire.begin();iter != fire.end();iter++)
			{
				printf("(%d %d %d) ",(*iter).i,(*iter).j,(*iter).depth);
			}
			printf("\n");
		
		}
	
	
	}
}
