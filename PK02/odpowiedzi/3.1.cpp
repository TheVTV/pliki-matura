#include <iostream>
#include <fstream>
#include <vector>
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
    plik.open("kebab.txt",ios::in);
    int tmp,champ=0;
    vector<int> kebaby;

    for(int i=0;i<750;i++)
    {
        plik>>tmp;
        if(kebab(tmp).second>=champ)
        {
            if(kebab(tmp).second>champ)
            {
                kebaby.clear();
                champ=kebab(tmp).second;
            }
            kebaby.push_back(tmp);
        }
    }
    cout<<champ<<endl;
        for(const auto &it : kebaby)
        {
            cout<<it<<endl;
        }
    return 0;
}
