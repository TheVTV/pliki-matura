#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <iomanip>

using namespace std;

int main(){
    ifstream in("pliki/liczby.txt");
    ofstream out("wynik2.txt", ios::app);
    
    string s1, s2;
    long long int suma=0;
    vector<long long int> v(17, 0);

    while(in >> s1 >> s2){
        suma+=s1.size()+s2.size();

        for(int i=0; i<s1.size(); i++){
            if(s1[i]<='9'){
                v[s1[i]-'0']++;
            }
            else{
                v[s1[i]-'A'+10]++;
            }
        }

        for(int i=0; i<s2.size(); i++){
            if(s2[i]<='9'){
                v[s2[i]-'0']++;
            }
            else{
                v[s2[i]-'A'+10]++;
            }
        }

    }

    for(int i=0; i<10; i++){
        out << setprecision(2) << fixed << i << ": " << v[i]*1.0/suma*100 << "%\n";
    }
    for(int i=0; i<6; i++){
        out << setprecision(2) << fixed << char(i+'A') << ": " << v[10+i]*1.0/suma*100 << "%\n";
    }

    return 0;
}