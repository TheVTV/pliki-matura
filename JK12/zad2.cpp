#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
int main(){
string liczba;
while(true){
cin>>liczba;
int n=liczba.size(),curr=0;
for(int i=0;n>i;i++){
    if(liczba[i]>curr){
        curr=liczba[i];
    }
}
if(curr>57){
    cout<<16-(curr-55)<<"\n";
}else{
    cout<<16-(curr-48)<<"\n";
}
}
    return 0;
}



