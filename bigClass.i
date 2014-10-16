%module bigClass
%{
/* Includes the header in the wrapper code */
#include "bigClass.h"
%}


/* Parse the header file to generate wrappers */
%include "bigClass.h"