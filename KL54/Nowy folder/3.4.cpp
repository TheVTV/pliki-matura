#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
bool czy_falafel(int a) {
    int suma_dzielnikow = 0;
    for (int i = 1; i <= sqrt(a); ++i) {
        if (a % i == 0) {
            suma_dzielnikow += i;
            if (i != 1 && i != a / i) {
                suma_dzielnikow += a / i;
            }
        }
    }

    return suma_dzielnikow == a;
}

int kebab_falafel(int a, int& dl) {
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
        return a + kebab_falafel(co, dl);
}

int main() {
    ifstream plik("kebab.txt");
    int liczba;
    int ile_falafeli = 0;

    while (plik >> liczba) {
        int dl = 1;
        int kebabowa = kebab_falafel(liczba, dl);

        if (czy_falafel(kebabowa))
            ile_falafeli++;
    }

    cout << ile_falafeli << endl;

    return 0;
}
