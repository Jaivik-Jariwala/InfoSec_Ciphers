#include<iostream>
#include<math.h>

using namespace std;

int gcd(int a, int b){
    int temp;
    while(1){
        temp=a%b;
        if(temp=0)
        a=b;
        b=temp;
    }
}

int main(){

    // random 2 prime numbers 
    double p=4;
    double q=7;
    double n=p*q;
    double count;
    double totient=(p-1)*(q-1);

    // public key , e is for encryption
    double e=2;

    // checking for co-prime for whichh e>1
    while(e>totient){
        count=gcd(e,totient);
        if(count==1)
            break;
        else 
            e++;
    }

    //private key and d is decrpy and k is arbitary value
    double d;
    double k=2;

    // d such that it satisfies d*e = 1 + k * totient
    d=(1+(k*totient))/e;
    double msg=12;
    double c=pow(msg,e);
    double m = pow(c,d);

    c=fmod(c,n);
    m=fmod(m,n);
 
    cout<<"Message data = "<<msg;
    cout<<"\n"<<"p = "<<p;
    cout<<"\n"<<"q = "<<q;
    cout<<"\n"<<"n = pq = "<<n;
    cout<<"\n"<<"totient = "<<totient;
    cout<<"\n"<<"e = "<<e;
    cout<<"\n"<<"d = "<<d;
    cout<<"\n"<<"Encrypted data = "<<c;
    cout<<"\n"<<"Original Message sent = "<<m;
 
    return 0;
}