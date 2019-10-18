#include <stdio.h>
#define K 1008
int main() 
{
int a,b,c,z;
for (a=1; a<=K; a++) {
for (b=a; b<=K; b++) {
for (c=b; c<=K; c++) {
z=a+b+c;
if (z>K) break;
if (z==K) if (a*a+b*b==c*c) printf("%d %d %d \n", a,b,c);	
}
}
}
}

