
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include "precision.h"
#include "smoother.h"


int main( int argc, char *argv[] )  {
  smoother smoothOperator;
  int nx, ny, nElements;
  int nIter;
  real dx;
  real *f, *smoothF;

  if( argc == 3 ) {
     nx = atoi(argv[1]);
     ny = nx;
     nElements = nx*ny;
     dx = 1.0/(real)nx;

     nIter = atoi(argv[2]);
  }
  else if( argc > 3 ) {
     printf("Too many arguments supplied.\n");
     return -2;
  }
  else {
     printf("Two argument expected.\n");
     return -1;
  }
  

  // Create the smoother
  smootherInit(&smoothOperator);

  // Allocate space for the function we want to smooth
  f  = (real*)malloc( nElements*sizeof(real) );
  smoothF = (real*)malloc( nElements*sizeof(real) );

  real y;
  real x;
  int iel;
  // Initialize the function we want to smooth and the smoothed function
  for( int iy=0; iy<ny; iy++ ){
    y = (real)iy*dx;
    for( int ix=0; ix<nx; ix++ ){
      x = (real)iy*dx;
      iel = ix + nx*iy;
      f[iel] = sin(x/10.0)*sin(y/10.0);
      smoothF[iel] = 0.0;
    }
  } 


  // Run the smoother
  smoothField( &smoothOperator, f, smoothF, nx, ny, nIter );


  // Free space
  free(f);
  free(smoothF);
  smootherFree(&smoothOperator);

  return 0;

}
