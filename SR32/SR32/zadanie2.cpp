#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>

using namespace std;

#define N 1000

typedef struct
{
    string a, b;
}pr;

vector<pr>V;

ofstream out("wyniki2.txt");

int OtherToDec(string s, int p)
{
    int d=0;
    for(int i=0; i<s.size(); i++)
    {
        if(s[i]<='9') d=d*p+s[i]-'0';
        else d=d*p+s[i]-'A'+10;
    }
    return d;
}

void Z2()
{
    map<int,int>M;
    for(pr v: V)
    {
        string a=v.a;
        string b=v.b;
        int x, y;
        for(int i=2; i<=16; i++)
        {
            string aa=to_string(OtherToDec(a,i));
            string bb=to_string(OtherToDec(b,i));
            reverse(bb.begin(), bb.end());
            if(aa==bb)
            {
                M[i]++;
                break;
            }
        }
    }
    cout<<"Zadanie 2.2."<<endl;
    out<<"Zadanie 2.2."<<endl;
    for(int i=2; i<=16; i++)
    {
        cout<<i<<": "<<M[i]<<endl;
        out<<i<<": "<<M[i]<<endl;
    }
    cout<<endl<<endl;
    out<<endl<<endl;
}

void Z3()
{

    vector<int>Sys;
    for(pr v: V)
    {
        string a=v.a;
        string b=v.b;
        int x, y;
        for(int i=2; i<=16; i++)
        {
            string aa=to_string(OtherToDec(a,i));
            string bb=to_string(OtherToDec(b,i));
            reverse(bb.begin(), bb.end());
            if(aa==bb)
            {
                Sys.push_back(i);
                break;
            }
        }
    }
    int mn=OtherToDec(V[0].a,Sys[0]);
    int mx=OtherToDec(V[0].a,Sys[0]);
    string mns=V[0].a;
    string mxs=V[0].a;

    for(int i=0; i<N; i++)
    {
        int x=OtherToDec(V[i].a,Sys[i]);
        int y=OtherToDec(V[i].b,Sys[i]);
        if(x>mx)
        {
            mx=x;
            mxs=V[i].a;
        }
        if(y>mx)
        {
            mx=y;
            mxs=V[i].b;
        }
        if(x<mn)
        {
            mn=x;
            mns=V[i].a;
        }
        if(y<mn)
        {
            mn=y;
            mns=V[i].b;
        }


    }

    cout<<"Zadanie 2.3."<<endl;
    out<<"Zadanie 2.3."<<endl;
    cout<<mns<<" "<<mxs;
    out<<mns<<" "<<mxs;
    cout<<endl<<endl;
    out<<endl<<endl;
}

void Z4()
{
    int c=0;
    map<int, float>M;
    for(pr v: V)
    {
        string a=v.a;
        string b=v.b;
        for(char z: a)
        {
            if(z<='9') M[z-'0']++;
            else M[z-'A'+10]++;
            c++;
        }
        for(char z: b)
        {
            if(z<='9') M[z-'0']++;
            else M[z-'A'+10]++;
            c++;
        }
    }
    cout<<"Zadanie 2.4."<<endl;
    out<<"Zadanie 2.4."<<endl;
    for(int i=0; i<=9; i++)
    {
        cout<<i<<": "<<round(M[i]*100*100/c)/100<<"%"<<endl;
        out<<i<<": "<<round(M[i]*100*100/c)/100<<"%"<<endl;
    }
    for(int i=10; i<=15; i++)
    {
        cout<<char(i-10+'A')<<": "<<round(M[i]*100*100/c)/100<<"%"<<endl;
        out<<char(i-10+'A')<<": "<<round(M[i]*100*100/c)/100<<"%"<<endl;
    }

}

int main()
{
    ifstream in("liczby.txt");
    if(!in.good()) cout<<"ERROR";
    for(int i=0; i<N; i++)
    {
        pr v;
        in>>v.a>>v.b;
        V.push_back(v);
    }

    Z2();
    Z3();
    Z4();

    in.close();
    out.close();
    return 0;
}
