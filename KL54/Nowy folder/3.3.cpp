#include<iostream>
#include<fstream>
using namespace std;

int kebab_mieciany(int a, int& parz, int& nieparz) {
    int suma = 0;
    int prev = -1;

    while (true) {
        suma += a;
        if (a % 2 == 0) parz++;
        else nieparz++;

        if (a == prev) break;

        int n = a;
        int co = 0;
        int t = 2;

        while (n > 1) {
            if (n % t == 0) {
                co += t;
                n /= t;
            } else {
                t++;
            }
        }

        prev = a;
        a = co;
    }

    return suma;
}

int main() {
    ifstream plik("kebab.txt");
    int liczba;
    int ile_miecianych = 0;

    while (plik >> liczba) {
        int parz = 0, nieparz = 0;
        kebab_mieciany(liczba, parz, nieparz);

        if (parz == nieparz)
            ile_miecianych++;
    }

    cout << ile_miecianych << endl;

    return 0;
}
