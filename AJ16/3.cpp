#include <bits/stdc++.h>

using namespace std;


int kebab_etap(int liczba){
    int res =0;

    while(liczba>1){
        for(int i=2;i<=liczba;i++){
            if (liczba%i==0){
                liczba /=i;
                res+=i;
                break;
            }
        }
    }


    return res;
}
int kebab_dl(int liczba){
    int dl=2;
    int prev = liczba;
    liczba=kebab_etap(liczba);

    while(liczba!=prev){
        prev = liczba;
        liczba=kebab_etap(liczba);
          dl+=1;
    }

    return dl;
}
int liczba_kebabowa(int liczba){
    int res=liczba;

    int prev = liczba;
    liczba=kebab_etap(liczba);

    while(liczba!=prev){
        res+=liczba;
        prev = liczba;
        liczba=kebab_etap(liczba);
    }
    res+=liczba;
    return res;
}

bool czy_pierwsza(int liczba){
    if (liczba<2) {
        return false;
    }
    for (int i=2; i*i<=liczba; i++){
        if (liczba%i==0){
            return false;
        }
    }
    return true;
}
bool czy_palindrom(int liczba){
    int n = liczba;
    int odwrocona = 0;
    while (n > 0) {
        odwrocona = odwrocona * 10 + n % 10;
        n /= 10;
    }
    return liczba == odwrocona;
}

int main()
{
    ifstream file("../pliki/kebab.txt");
    string line;
    vector<int> liczby;

    while(getline(file,line)){
        liczby.push_back(stoi(line));
    }

    //3.1
    int dl_max=0;
    vector<int> dl_max_liczby;
    for (int i=0;i<liczby.size();i++){
            int dl=kebab_dl(liczby[i]);
            if(dl>dl_max){
                dl_max=dl;
                dl_max_liczby.clear();
                dl_max_liczby.push_back(liczby[i]);
                continue;
            }
            if(dl==dl_max){
                dl_max_liczby.push_back(liczby[i]);
            }

    }
    cout<<"3.1"<<endl;
    cout<<dl_max<<endl;
    for(int i =0;i<dl_max_liczby.size();i++){
        cout<<dl_max_liczby[i]<<endl;
    }

    //3.2
    int liczba_palindromow=0;
    int liczba_liczb_pierwszych=0;
    for (int i=0;i<liczby.size();i++){
        int kebabowa = liczba_kebabowa(liczby[i]);

        if (czy_pierwsza(kebabowa)){
            liczba_liczb_pierwszych+=1;
        }
        if (czy_palindrom(kebabowa)){
            liczba_palindromow+=1;
        }
    }
    cout<<endl<<"3.2"<<endl;
    cout<<liczba_palindromow<<" "<<liczba_liczb_pierwszych<<endl;


    //3.3

    int liczba_mieszanych=0;
    for (int i=0;i<liczby.size();i++){
        int mieszany=0;
        int liczba = liczby[i];

        if (liczba%2==0){
            mieszany+=1;
        } else {
            mieszany-=1;
        }
        int prev = liczba;
        liczba=kebab_etap(liczba);
        if (liczba%2==0){
            mieszany+=1;
        } else {
            mieszany-=1;
        }

        while(liczba!=prev){
            prev = liczba;
            liczba=kebab_etap(liczba);
        if (liczba%2==0){
            mieszany+=1;
        } else {
            mieszany-=1;
        }
        }
        if(mieszany==0){
            liczba_mieszanych+=1;
        }
    }

    cout<<endl<<"3.3"<<endl;
    cout<<liczba_mieszanych<<endl;


    //3.4
    int falafele=0;
    for (int i=0;i<liczby.size();i++){
        int kebabowa = liczba_kebabowa(liczby[i]);
        int suma=0;

        for (int j=1;j<kebabowa;j++){
            if (kebabowa%j==0){
                suma+=j;
            }
        }
        if (suma==kebabowa){
            falafele+=1;
        }
    }

    cout<<endl<<"3.4"<<endl;
    cout<<falafele<<endl;


    cin.get();
    return 0;
}
