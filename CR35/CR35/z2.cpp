#include <bits/stdc++.h> 

using namespace std;

string tab[1000][2];
int t2[1000][2];
int s[1000];

int zam(string n, int L, int s) {
    int w = 0;
    if (n[0] > '9') w = int(n[0]) - 55;
    else w = int(n[0]) - 48;
    if (L > 1) {
        for (int i = 1; i < L; i++) {
            w *= s;
            if (n[i] > '9') w += int(n[i]) - 55;
            else w += int(n[i]) - 48;
        }
    }
    return w;
}

void z22() {
    string a, b;
    int w[15] = { 0 };
    for (int i = 0; i < 1000; i++) {
        for (int j = 2; j <= 16; j++) {
            t2[i][0] = zam(tab[i][0], tab[i][0].length(), j);
            t2[i][1] = zam(tab[i][1], tab[i][1].length(), j);
            a = to_string(t2[i][0]);
            b = to_string(t2[i][1]);
            reverse(b.begin(), b.end());
            if (a == b) {
                s[i] = j;
                w[j - 2]++;
                break;
            }
        }
    }
    fstream zapis("wyniki2.txt", ios::out);
    zapis << "2.2:\n";
    for (int i = 0; i < 15; i++) {
        zapis << i + 2 << ": " << w[i] << endl;
    }
    zapis << "\n\n";
    zapis.close();
}

void z23() {
    int ma=t2[0][0], mi=t2[0][0], ima=0, jma=0, imi=0, jmi=0;
    for (int i = 0; i < 1000; i++) {
        for (int j = 0; j < 2; j++) {
            if (ma < t2[i][j]) {
                ma = t2[i][j];
                ima = i;
                jma = j;
            }
            if (mi > t2[i][j]) {
                mi = t2[i][j];
                imi = i;
                jmi = j;
            }
        }
    }
    fstream zapis("wyniki2.txt", ios::app);
    zapis << "2.3:\n" << tab[imi][jmi] << " " << tab[ima][jma] << "\n\n";
    zapis.close();
}

void z24() {
    int w[16] = { 0 };
    int lz = 0, p = 0;
    for (int i = 0; i < 1000; i++) {
        for (int j = 0; j < tab[i][0].length(); j++) {
            if (tab[i][0][j] > '9') w[tab[i][0][j] - 55]++;
            else w[tab[i][0][j] - 48]++;
            lz++;
        }
        for (int j = 0; j < tab[i][1].length(); j++) {
            if (tab[i][1][j] > '9') w[tab[i][1][j] - 55]++;
            else w[tab[i][1][j] - 48]++;
            lz++;
        }
    }
    float x;
    fstream zapis("wyniki2.txt", ios::app);
    zapis << "2.4:\n";
    for (int i = 0; i < 10; i++) {
        x = round(w[i] * 10000 / lz) / 100;
        zapis << i << ": " << x << "%\n";
    }
    for (int i = 10; i < 16; i++) {
        x = round(w[i] * 10000 / lz) / 100;
        zapis << char(55+i) << ": " << x << "%\n";
    }
    zapis.close();
}

int main()
{
    fstream plik("liczby.txt", ios::in);
    for (int i = 0; i < 1000; i++) plik >> tab[i][0] >> tab[i][1];
    plik.close();
    z22();
    z23();
    z24();
}