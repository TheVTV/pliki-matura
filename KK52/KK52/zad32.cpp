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
bool pierwsza(int a)
{
    if(a<2)
        return false;
    for(int i=2;i*i<=a;i++)
    {
        if(a%i==0)
            return false;
    }
    return true;
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
   int keb=0;
    for(int j=0;j<750;j++)
    {
        int k=0;
        keb=0;
        q=tab[j][0];
        while(q!=k)
        {
            keb=keb+q;
            k=q;
            q=czynniki(q);
        }
        tab[j][1]=keb+q;

    }
    int d=0;
    for (int i=0;i<750;i++)
    {
        if(pierwsza(tab[i][1]))
            d++;

    }
    cout<<d;

}
