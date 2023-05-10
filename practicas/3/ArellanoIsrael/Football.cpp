//PROBLEMA CODEFORCES FUTBOLL
#include <bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[])
{
    string pal;
    cin >> pal;
    int contadorC, contadorU;
    for (int i = 0; i < pal.size(); i++)
    {
        if (pal[i]=='0')
        {
            contadorC++;
            contadorU=0;
        }
        else if(pal[i]=='1')
        {
            contadorU++;
            contadorC=0;
        }
        if (contadorC == 7 || contadorU == 7 )
        {
            cout << "YES"<<endl;
        }
        else
        {
            cout << "NO"<<endl;
        }
        
    }
    return 0;
}
