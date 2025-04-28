#include <bits/stdc++.h>
using namespace std;

int czynniki(int a)
{
    int k=0;
    for(int i=2;i<=a;i++)
    {
        if(a%i==0)
        {
            a=a/i;
            i--;
            k=k+i+1;
        }
    }
    return k;
}
int main()
{
    int tab[750][2];
    ifstream plik;
    plik.open("kebab.txt",ios::in);
    if(!plik.good())
        cout<<"aaa";
    for(int i=0;i<750;i++)
    {
        plik >> tab[i][0];
    }
   int q=0;
   int wmax=0;
    for(int j=0;j<750;j++)
    {
         int w=1;
        int k=0;
        q=tab[j][0];
        while(q!=k)
        {
            k=q;
            q=czynniki(q);
            w++;
        }
        tab[j][1]=w;
        if(w>wmax)
        {wmax=w;
        }
    }
    cout<<wmax<<endl;
    for(int b=0;b<750;b++)
    {
        if(tab[b][1]==wmax)
            cout<<tab[b][0]<<endl;
    }

}
