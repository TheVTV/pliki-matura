#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

pair<int,int> kebab(int liczba)
{
    vector<int> v;
    int i,start,koniec=liczba,licznik=0,value=0,start2;
    while(start!=koniec)
    {
        i=2;
        v.push_back(koniec);
        licznik++;
        start=koniec;
        start2=koniec;
        koniec=0;
        while(start>1)
        {
            if(start%i==0)
            {
                start/=i;
                koniec+=i;
            }
            else
            {
                i++;
            }
        }
        if(start2==koniec)
            break;
    }
    for(const auto &it : v)
    {
        value+=it;
    }
    return {value,licznik+1};
}

int main()
{
    fstream plik;
    plik.open("kebab_przyklad.txt",ios::in);
    string pal1,pal2;
    int pals=0,tmp,prime=0;
    bool flag;
    while(plik.good())
    {
        plik>>tmp;
        pal1=to_string(kebab(tmp).first);
        pal2="";
        flag=true;
        for(int i=0;i<pal1.length();i++)
        {
            pal2[i]=pal1[pal1.length()-i-1];
        }
        if(pal1==pal2)
        {
            pals++;
        }
        for(int i=0;i<sqrt(tmp);i++)
        {
            if(tmp%i==0)
            {
                flag=false;
                break;
            }
        }
        if(flag)
        {
            prime++;
        }
    }
    return 0;
}
