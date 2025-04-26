#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
using namespace std;

bool czy_pierw(int n) {

    if (n <2) return false;
    if (n%2 == 0) {
        if (n == 2)return true;
        else return false;
    }

    int temp = 3;
    while (temp < sqrt(n)) {
        if (n%temp == 0)return false;
        temp++;
    }
    return true;
}

int suma(int x) {

    int temp =2, wynik=0;


    while (x > 1) {
        if (x%temp == 0) {
            if (czy_pierw(temp)) {
                x=x/temp;
                wynik+=temp;
                temp=2;
            }
        }
        else temp++;
    }

    cout << '\n';
    return wynik;
}

bool czy_poli(int x) {
    string str = to_string(x);
    for (int i =0; i < str.length()/2; i++) {
        if (str[i] != str[str.length()-1-i])return false;
    }
    return true;
}

int main() {
    int zad =2;
    int number =750;
    ifstream fin ("kebab.txt");

    if (zad == 1) {
        int x, pop, maks=0;
        vector<int>vec;

        for (int i =0; i < number;i++) {
            fin >> x;

            int dl=3;

            pop = suma(x);
            while (pop != suma(pop)) {
                pop = suma(pop);
                dl++;
            }

            if (dl > maks) {
                maks = dl;
                vec.clear();
                vec.push_back(x);
            }
            else if (dl == maks) {
                vec.push_back(x);
            }
        }

        cout << maks << '\n';
        for (int i =0; i < vec.size(); i++) {
            cout << vec[i] << '\n';
        }
    }

    if (zad == 2) {
        int x, pop, kebab, wyniki1=0, wyniki2=0;
        vector<int>vec;

        for (int i =0; i < number;i++) {
            fin >> x;
            kebab = x;
            pop =x;

            while (pop != suma(pop)) {
                pop = suma(pop);
                kebab+=pop;
            }
            kebab+=pop;

            if (czy_pierw(kebab))wyniki1++;
            if (czy_poli(kebab))wyniki2++;
        }

        cout << wyniki1 << " " << wyniki2 << '\n';
    }

    if (zad == 2) {
        int x, pop, parz, nparz, wynik=0;
        vector<int>vec;

        for (int i =0; i < number;i++) {
            fin >> x;
            parz=0;
            nparz=0;

            if (x%2 == 0)parz++;
            else nparz++;

            pop =x;

            while (pop != suma(pop)) {
                pop = suma(pop);
                if (pop%2 == 0)parz++;
                else nparz++;
            }
            if (pop%2 == 0)parz++;
            else nparz++;

            if (nparz == parz)wynik++;
        }

        cout << wynik << '\n';
    }
}