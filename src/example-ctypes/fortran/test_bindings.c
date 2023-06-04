#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double averagefnc_abstract(double(*func)(double*), double*, double*);
double averagefnc_explicit(double(*func)(double*), double*, double*);

double func(double* x){
   return *x;
}

int main(){
   double a = 1.;
   double b = 2.;
   printf("%lf\n", averagefnc_abstract(func, &a, &b));
   a = 3.;
   b = 4.;
   printf("%lf\n", averagefnc_explicit(func, &a, &b));
}