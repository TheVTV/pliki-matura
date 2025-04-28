#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
bool tab[10000]={0};

bool gen1(long long a){
for(int i=2;a>i;i++){
if(a%i==0) return false;}
return true;}
int zwijacz(long long a=0){
    int zwiniete=0;
    for(int i=a;i>1;i--){
        if(a%i==0&&gen1(i)==1){
            zwiniete=zwiniete+i;
            a=a/i;
            i++;
        }}
        return zwiniete;
}
int main(){
int a,b=-1,i=1;
cin>>a;
tab[0]=zwijacz(a);
while(true){
    a=zwijacz(a);
    tab[i]=zwijacz(a);
    b=zwijacz(a);
    tab[i+1]=zwijacz(a);
    i++;
    if(a==b)break;
}
cout<<i+1;
cout<<tab[0];
cout<<tab[1];
cout<<tab[2];

return 0;
}
