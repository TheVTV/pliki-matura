#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int kebab(int a, int& dl) {
    int co = 0;
    int t = 2;
    int n = a;

    while (n > 1) {
        if (n % t == 0) {
            co += t;
            n /= t;
        }
        else {
            t++;
        }
    }

    dl++;

    if (co == a)
        return a;
    else
        return a + kebab(co, dl);
}

int main() {
    ifstream plik("kebab_przyklad.txt");
    int liczba;

    int max_dlugosc = 0;
    vector<int> liczby_max;

    while (plik >> liczba) {
        int dl = 1;
        kebab(liczba, dl);

        if (dl > max_dlugosc) {
            max_dlugosc = dl;
            liczby_max.clear();
            liczby_max.push_back(liczba);
        }
        else if (dl == max_dlugosc) {
            liczby_max.push_back(liczba);
        }
    }

    cout << max_dlugosc << endl;
    for (int x : liczby_max)
        cout << x << endl;

    return 0;
}
