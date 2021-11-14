#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;
void avg(int a[]){
    int sum = 0;
    for (int i = 0; i < 100; i++)
    {
        sum += a[i];
    }
    int avg = sum / 100;
    cout<<"Average: "<<avg<<endl;
}
void max(int a[]){
    int max = 0;
    for (int i = 0; i < 100; i++)
    {
        if (max < a[i])
        {
            max = a[i];
        }
    }
    cout << "Maximum value: " << max << endl;
}
void min(int a[]){
    int min = 1000000;
    for (int i = 0; i < 100; i++)
    {
        if (min > a[i])
        {
            min = a[i];
        }
    }
    cout << "Minimum value: " << min << endl;
}
void pavg(int a[]){
    for (int i = 0; i < 10; i++)
    {
        int result = 0;
        for (int j = 0; j < 10; j++)
        {
            result += a[i*10+j];
        }
        result /= 10;
        cout << "Average for "<<i+1<<" sequence is:"<< result << endl;
    }
}
int main(){
    srand(time(NULL));
    int a[101];
    for (int i = 0; i < 100; i++)
    {
        a[i] = rand();
    }
    string s;
    cin>>s;
    if (s == "avg")
    {
        avg(a);
    }
    else if (s == "max"){
        max(a);
    }
    else if (s == "min"){
        min(a);
    }
    else if (s == "pavg"){
        pavg(a);
    }
    
}