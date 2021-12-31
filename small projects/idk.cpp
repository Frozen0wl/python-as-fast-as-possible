#include <iostream>
#include <stdio.h>      /* printf */
#include <math.h>       /* pow */
using namespace std;

int main ()
{
  for(int i = 0; i< 10000000; i++){
    cout << pow(i, i) << std::endl;
  }
  return 0;
}