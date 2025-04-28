#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

#define N 750

vector<int>V;

ofstream out("wyniki3.txt");

int SumCzyn(int n)
{
    int suma=0;
    int d=2;
    while(d*d<=n)
    {
        if(n%d==0)
        {
            suma+=d;
            n/=d;
        }
        else d++;
    }
    suma+=n;
    return suma;
}

void Z1()
{
    vector<int>R;
    int mc=2;
    for(int v: V)
    {
        int a=v;
        int c=2;
        while(true)
        {
            int b=SumCzyn(a);
            if(b==a) break;
            c++;
            a=b;
        }
        if(c==mc)
        {
            R.push_back(v);
        }
        if(c>mc)
        {
            mc=c;
            R.clear();
            R.push_back(v);
        }
    }
    cout<<"Zadanie 3.1."<<endl;
    out<<"Zadanie 3.1."<<endl;
    cout<<mc<<endl;
    out<<mc<<endl;
    for(int r: R)
    {
        cout<<r<<endl;
        out<<r<<endl;
    }
    cout<<endl;
    out<<endl;
}

bool Pierwsza(int n)
{
    if(n<=1) return false;
    for(int i=2; i<=n/2; i++)
        if(n%i==0) return false;
    return true;
}

void Z2()
{
    int cpal=0;
    int cpie=0;

    for(int v: V)
    {
        int a=v;
        int lk=v;
        while(true)
        {
            int b=SumCzyn(a);
            lk+=b;
            if(b==a) break;
            a=b;
        }
        string s=to_string(lk);
        string rs=s;
        reverse(rs.begin(), rs.end());
        if(rs==s) cpal++;
        if(Pierwsza(lk)) cpie++;
    }
    cout<<"Zadanie 3.2."<<endl;
    out<<"Zadanie 3.2."<<endl;
    cout<<cpal<<" "<<cpie;
    out<<cpal<<" "<<cpie;
    cout<<endl<<endl;
    out<<endl<<endl;
}

void Z3()
{
    int ck=0;
    for(int v: V)
    {
        vector<int>L;
        int a=v;
        L.push_back(a);
        while(true)
        {
            int b=SumCzyn(a);
            L.push_back(b);
            if(b==a) break;
            a=b;
        }
        int cp=0, cn=0;
        for(int l: L)
        {
            if(l%2==0) cp++;
            else cn++;
        }
        if(cp==cn)
            ck++;
    }
    cout<<"Zadanie 3.3."<<endl;
    out<<"Zadanie 3.3."<<endl;
    cout<<ck<<endl<<endl;
    out<<ck<<endl<<endl;
}

int SumWl(int n)
{
    int suma=1;
    for(int i=2; i<=n/2; i++)
    {
        if(n%i==0) suma+=i;
    }
    return suma;
}

void Z4()
{
    int c=0;
    for(int v: V)
    {
        int a=v;
        int lk=v;
        while(true)
        {
            int b=SumCzyn(a);
            lk+=b;
            if(b==a) break;
            a=b;
        }
        if(SumWl(lk)==lk) c++;
    }
    cout<<"Zadanie 3.4."<<endl;
    out<<"Zadanie 3.4."<<endl;
    cout<<c;
    out<<c;
}

int main()
{
    ifstream in("kebab.txt");
    if(!in.good()) cout<<"ERROR";

    for(int i=0; i<N; i++)
    {
        int v; in>>v;
        V.push_back(v);
    }
    Z1();
    Z2();
    Z3();
    Z4();

    in.close();
    out.close();
    return 0;
}
