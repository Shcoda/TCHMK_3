%module bNum
%{
/* Includes the header in the wrapper code */
#include "bNum.h"
%}


/* Parse the header file to generate wrappers */
%include "bNum.h"