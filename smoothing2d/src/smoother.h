
#include "precision.h"

typedef struct smoother{
  int dim;
  real *weights;
}smoother;

// Manual Constructor : Allocates space for the interpolant
void smootherInit( struct smoother *smoothOperator);

// Manual Destructor : Frees space held by the interpolant
void smootherFree( struct smoother *smoothOperator );

// Additional routines
void smoothField( struct smoother *smoothOperator, real *f, real *smoothF, int nX, int nY);
