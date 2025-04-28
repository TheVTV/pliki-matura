#include <bits/stdc++.h>

using namespace std;

int tab[750];
int lz[750];
int lk[750];
int np[750][2] = { 0 };

bool czyP(int n) {
    for (int i = 2; i * i < n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

bool czyPali(int n) {
    string a, b;
    a = to_string(n);
    b = to_string(n);
    reverse(b.begin(), b.end());
    if (a == b) return true;
    return false;
}

void z31() {
    int mz = 0;
    int l, z, m, a, b, k;
    for (int i = 0; i < 750; i++) {
        l = tab[i];
        lk[i] = l;
        if (l % 2 == 0) np[i][0]++;
        else np[i][1]++;
        a = l;
        k = 0;
        m = 2;
        while (l > 1) {
            if (l % m == 0) {
                l /= m;
                k += m;
            }
            else m++;
        }
        lk[i] += k;
        if (k % 2 == 0) np[i][0]++;
        else np[i][1]++;
        b = k;
        z = 2;
        while (a != b) {
            l = b;
            k = 0;
            m = 2;
            while (l>1) {
                if (l % m == 0) {
                    l /= m;
                    k += m;
                }
                else m++;
            }
            a = b;
            lk[i] += k;
            if (k % 2 == 0) np[i][0]++;
            else np[i][1]++;
            b = k;
            z++;
        }
        lz[i] = z;
        if (mz < z) mz = z;
    }
    fstream zapis("wyniki3.txt", ios::out);
    zapis << "3.1:\n" << mz;
    for (int i = 0; i < 750; i++) {
        if (lz[i] == mz) zapis << endl << tab[i];
    }
    zapis << "\n\n";
    zapis.close();
}

void z32() {
    int p = 0, pali = 0;
    for (int i = 0; i < 750; i++) {
        if (czyP(lk[i])) p++;
        if (czyPali(lk[i])) pali++;
    }
    fstream zapis("wyniki3.txt", ios::app);
    zapis << "3.2:\n" << pali << " " << p << "\n\n";
    zapis.close();
}

void z33() {
    int w = 0;
    for (int i = 0; i < 750; i++) {
        if (np[i][0] == np[i][1]) w++;
    }
    fstream zapis("wyniki3.txt", ios::app);
    zapis << "3.3:\n" << w << "\n\n";
    zapis.close();
}

void z34() {
    int w = 0;
    int a;
    for (int i = 0; i < 750; i++) {
        a = 1;
        for (int j = 2; j < lk[i]; j++) {
            if (lk[i] % j == 0) a += j;
        }
        if (a == lk[i]) w++;
    }
    fstream zapis("wyniki3.txt", ios::app);
    zapis << "3.4:\n" << w;
    zapis.close();
}

int main()
{
    fstream plik("kebab.txt", ios::in);
    for (int i = 0; i < 750; i++) plik >> tab[i];
    plik.close();

    z31();
    z32();
    z33();
    z34();
}