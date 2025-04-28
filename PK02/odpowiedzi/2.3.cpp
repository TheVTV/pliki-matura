#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
int sys(string napis)
{
    char champ=napis[0];
    for(int i=1;i<napis.length();i++)
    {
        if(champ<=napis[i])
        {
            champ=napis[i];
        }
    }
    if(champ>='A')
    {
        return int(champ-'A')+11;
    }
    return int(champ-'0')+1;
}

int F(char a)
{
    if(a>='A')
    {
        return int(a-'A'+10);
    }
    return int(a-'0');
}

int value(string napis, int sys)
{
    int valuer=0;
    for(int i=0;i<napis.length();i++)
    {
        valuer+=pow(sys,i)*F(napis[napis.length()-i-1]);
    }
    return valuer;
}
int main()
{
    pair<string,string> liczby;
    fstream plik;
    plik.open("liczby.txt",ios::in);
    string maximus="11",minimus="FFFFF";
    while(plik.good())
    {
        plik>>liczby.first;
        plik>>liczby.second;
        if(value(liczby.first,sys(liczby.first))>value(maximus,sys(maximus)))
        {
            maximus=liczby.first;
        }
        if(value(liczby.second,sys(liczby.second))>value(maximus,sys(maximus)))
        {
            maximus=liczby.second;
        }
        if(value(liczby.first,sys(liczby.first))<=value(minimus,sys(minimus)))
        {
            minimus=liczby.first;
        }
        if(value(liczby.second,sys(liczby.first))<=value(minimus,sys(minimus)))
        {
            minimus=liczby.second;
        }
    }
    cout<<minimus<<" "<<maximus;
    return 0;
}
