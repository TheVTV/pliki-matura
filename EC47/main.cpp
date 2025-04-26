#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;



int zmiana(string str, int base) {

    int len = str.length()-1;
    int wynik=0;
    int x;


    for (int i =0; i <str.length(); i++) {
        if (str[i] < 65)x = str[i]-48;
        else x=str[i]-55;


        wynik+=x*pow(base, len);
        len--;
    }

    return wynik;
}

string odwroc(string str) {
    string wyn="";
    for (int i =str.length()-1; i >=0; i--) {
        wyn+=str[i];
    }

    return wyn;
}

bool znajdz(string str1, string str2, int base)
{
    int x1 = zmiana(str1, base);
    int x2 = zmiana(str2, base);
    string y1 = to_string(x1);
    string y2 = to_string(x2);
    string y3;
    y3 = odwroc(y2);

    if (y3 == y1)return true;
    else return false;

}

int main()
{
    int number = 1000;
    ifstream fin ("liczby.txt", ios::in);

    int zad=3;

    if (zad == 1) {
        string str, str2;
        int x1, x2;

        int tab[15]={0};

        for (int i =0; i < number; i++) {
            fin >> str;
            fin >> str2;

            for (int i =2;i < 17; i++) {
                if (znajdz( str,  str2,  i)) {
                    tab[i-2]++;
                    i = 17;
                }
            }
        }


        for (int i =0; i < 15; i++) {
            cout << i+2 << " " << tab[i] << '\n';
        }
    }

    if (zad == 2) {
        string str, str2, maks_s, mini_s;
        int x1, x2, maks=0, mini=INT_MAX;


        for (int i =0; i < number; i++) {
            fin >> str;
            fin >> str2;


            for (int i =2;i < 17; i++) {
                if (znajdz( str,  str2,  i)) {
                    x1 = zmiana(str, i);
                    if (maks < x1) {
                        maks = x1;
                        maks_s = str;
                    }
                    if (mini > x1) {
                        mini = x1;
                        mini_s = str;
                    }

                    x2 = zmiana(str2, i);
                    if (maks < x2) {
                        maks = x2;
                        maks_s = str2;
                    }
                    if (mini > x2) {
                        mini = x2;
                        mini_s = str2;
                    }
                    i=17;
                }
            }
        }
        cout << mini_s << " " << maks_s << '\n';
    }

    if (zad == 3) {
        float tab[16]={0};
        float razem=0;
        int temp;
        string str, str2;

        for (int i =0; i < number; i++) {
            fin >> str;
            razem+=str.length();

            for (int i =0;  i < str.length(); i++) {
                temp = str[i];
                if (str[i] < 65)temp = str[i]-48;
                else temp=str[i]-55;

                tab[temp]++;
            }

            fin >> str;
            razem+=str.length();

            for (int i =0;  i < str.length(); i++) {
                temp = str[i];
                if (str[i] < 65)temp = str[i]-48;
                else temp=str[i]-55;

                tab[temp]++;
            }

        }
        cout << razem << '\n';

        for (int i =0; i < 16;i++) {
            cout << i << ": " << (tab[i]/razem)*100 << "%" << '\n';
        }
    }

}