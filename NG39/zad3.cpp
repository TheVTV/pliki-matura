#include <iostream>
#include <fstream>
#include<vector>
using namespace std;

constexpr int N=750;
ofstream out("wyniki3.txt");
vector<int> V;

int sumaCz(int n)
{
    int d=2, suma=0;
    while(n>1)
    {
            while(n%d==0)
            {
                suma=suma+d;
                n=n/d;
            }
            d++;
    }
    return suma;
}

int Zwij(int n)
{
    int c=1, licz=1;
    while(c>0)
    {
        c=sumaCz(n);
        if(c==n)
            c=-1;
        else
            n=c;
        licz++;
    }
    return licz;
}

void Zad3_1()
{
    vector<int> kebs;
    int maksl, maks=0, zwijanie;
    for(int i=0; i<N; i++)
    {
        zwijanie=Zwij(V[i]);
        if(zwijanie==maks)
            kebs.push_back(V[i]);
        if(zwijanie>maks)
        {
            maks=zwijanie;
            kebs.clear();
            kebs.push_back(V[i]);
        }
    }
    out << "Zadanie 3_1: " << endl << "ilosc zwijania: " << maks << " liczba/y: ";
    for(int i=0; i<kebs.size(); i++)
        out << kebs[i] << " ";
    out << endl;
}

int KEBAB(int n)
{
   int suma=n, c=1, licz=1;
    while(c>0)
    {
        c=sumaCz(n);
         suma=suma+c;
        if(c==n)
            c=-1;
        else
            n=c;

    }
    return suma;
}

bool Pierwsza(int n)
{
    if(n==1)
        return false;
    int d=5;
    if(n==2 || n==3)
        return true;
    if(n%2==0 || n%3==0)
        return false;
    while(d*d<=n)
    {
        if(n%d==0 || n%(d+2)==0)
            return false;
        d=d+6;
    }
    return true;
}


bool Palindrom(int n)
{
    string s="";
    while(n>0)
    {
        s=char(n%10 +'0') +s;
        n=n/10;
    }
    int j=s.size()-1;
    for(int i=0; i<j; i++, j--)
        if(s[i]!=s[j])
            return false;
        return true;
}
void Zad3_2()
{
    int pali=0, p=0;
    int kebsowa;
    for(int i=0; i<N; i++)
    {
         kebsowa=KEBAB(V[i]);
         if(Palindrom(kebsowa))
            pali++;
         if(Pierwsza(kebsowa))
            p++;
    }
    out << "Zadanie 3_2: " << endl;
    out << pali << " " << p;
    out << endl;
}

bool Mieciany(int n)
{
    int p=0, np=0, c=1, licz=1;
    if(n%2==0)
        p++;
    else
        np++;

    while(c>0)
    {

        c=sumaCz(n);
        if(c%2==0)
            p++;
        else
            np++;
        if(c==n)
            c=-1;
        else
            n=c;

    }
    if(p==np)
        return true;
    return false;
}

void Zad3_3()
{
    int licz=0;
    for(int i=0; i<N; i++)
    {
        if(Mieciany(V[i]))
            licz++;
    }
    out << "Zad 3_3: " << endl << licz << endl;
}

bool Falafel(int n)
{
    int p=n, d=1, f=0;
    while(d<p/2)
    {
        if(p%d==0)
            f=f+d;
        d++;
    }
    if(f==n)
        return true;

    return false;
}

void Zad3_4()
{
    int licz=0, n;
    for(int i=0; i<N; i++)
    {
        n=KEBAB(V[i]);
        if(Falafel(n))
            licz++;
    }
    out << "zad 3_4: " << endl << licz << endl;
}

int main()
{
    int n;
    ifstream in("kebab.txt");
    if(in.is_open())
    {
        for(int i=0; i<N;i++)
        {
             in >> n;
             V.push_back(n);
        }
    }
    else
        cout << "err";

    Zad3_1();
    Zad3_2();
    Zad3_3();
    Zad3_4();

    return 0;
}
