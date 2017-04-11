#include "factorial-tail.h"

int facttail(int n, int a)
{
  if (n < 0) return 0;
  else if (n == 0) return 1;
  else if (n == 1) return a;
  else return facttail(n -1, n * a);
}
