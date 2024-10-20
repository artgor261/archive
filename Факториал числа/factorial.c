#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>

void fact(mpz_t num){
     mpz_t i, result;
     int cmp_result;
     
     mpz_init(i);
     mpz_init(result);
     mpz_set_ui(result, 1);
     mpz_set_ui(i, 1);
     cmp_result = mpz_cmp(num, i);
     
     while (cmp_result >= 0){
           mpz_mul(result, result, i);
           mpz_add_ui(i, i, 1UL);
           cmp_result = mpz_cmp(num, i);
     }
     
     printf("Factorial: ");
     mpz_out_str(stdout, 10, result);
     mpz_clear(i);
     mpz_clear(result);
}

int main(){
   char str[51];
   mpz_t num;
   
   printf("Print number: ");
   scanf("%50s", str);
   mpz_init(num);
   mpz_set_str(num, str, 10);
   fact(num);
   mpz_clear(num);
   printf("\n");
   return 0;
}
