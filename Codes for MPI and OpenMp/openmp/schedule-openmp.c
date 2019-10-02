/*****************************************************************************
About: OpenMP program to see scheduling(static,dynamic,guided) of loop iterations 
       among threads. 
       export OMP_SCHEDULE=dynamic,4   //change chunksize to different values
       export OMP_NUM_THREADS=4        //change no. of threads to different values
*****************************************************************************/

#include<stdio.h>
#include<omp.h>
#include<unistd.h>
int main()
{
 int i,tid;

 #pragma omp parallel private(tid)
 {
  tid=omp_get_thread_num();
 #pragma omp for schedule(runtime)
 for(i=0;i<20;i++)
 {
   printf("i=%3d tid=%d\n",i,tid);
   sleep(4);
 }
 }

 return 0;
}

