#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool pierwsze[1000000];


void sito()
{
    for(int i = 2; i<1000000; i++) pierwsze[i] = true;
    pierwsze[1] = false;
    pierwsze[0] = false;
    for(int i = 2; i<1000000; i++)
    {
        if (pierwsze[i])
            for(int j = i+i; j<1000000; j+=i)
                pierwsze[j] = false;
    }
}

int sumarozkladu(int liczba)
{
    int suma = 0;
    while(true)
    {
        if(pierwsze[liczba])
        {
            suma += liczba;
            return suma;
        }
    for(int i = 2; i*i<=liczba; i++)
    {
        if(pierwsze[i])
        {
            if(liczba%i==0)
            {
                liczba/=i;
                suma += i;
                break;
            }
        }
    }
    }
}

bool czyPalindrom(int liczba)
{
    string s = to_string(liczba);
    for(int i = 0; i+i<=s.size()-1 ;i++)
    {
        if(s[i]!=s[s.size()-1-i])
            return false;
    }
    return true;
}

int main()
{
    sito();
    fstream plik;
    plik.open("kebab.txt");
    int Tab[750][4];
    for(int i=0; i<750; i++)
    {
        plik >> Tab[i][0];
        int liczba = Tab[i][0];
        Tab[i][1] = liczba;
        Tab[i][2] = 1;
        Tab[i][3] = liczba%2;
        int sum = 0;
        while(sum != liczba)
        {
            sum = liczba;
            liczba = sumarozkladu(liczba);
            Tab[i][1] += liczba;
            Tab[i][2] += 1;
            Tab[i][3] += liczba%2;
        }
    }
    int maxdlugosc = 0;
    for(int i=0; i<750; i++)
    {
        maxdlugosc = max(maxdlugosc, Tab[i][2]);
    }
    cout << "zadanie 3.1: \n" << maxdlugosc<<"\n";
    for(int i=0; i<750; i++)
    {
        if(Tab[i][2]==maxdlugosc) cout << Tab[i][0] <<"\n";
    }
    int iloscPalindromow = 0;
    int iloscPierwszych = 0;
    for(int i=0; i<750; i++)
    {
        if(pierwsze[Tab[i][1]])
            iloscPierwszych++;
        if(czyPalindrom(Tab[i][1]))
            iloscPalindromow++;
    }
    cout << "zadanie 3.2: \n" << iloscPalindromow << " " << iloscPierwszych <<"\n";
    int mieszany = 0;
    for(int i=0; i<750; i++)
    {
        if(Tab[i][3]+Tab[i][3]== Tab[i][2]) mieszany++;
    }
    cout << "zadanie 3.3: \n" << mieszany <<"\n";
    int falafel = 0;
    for(int i=0; i<750; i++)
    {
        int sumka = 1;
        for(int j = 2; j<Tab[i][1]; j++)
        {
            if(Tab[i][1]%j==0) sumka+=j;
        }
        if(sumka==Tab[i][1]) falafel++;

    }
    cout << "zadanie 3.4: \n" << falafel <<"\n";
}
