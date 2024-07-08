int x;

int myFunc(int y, int x) {
  return y + x;
}

char myFunc2(int x, char y) {
  return y;
}

int myFunc3(int a, int b) {
  return a - b;
}

int myFunc4(int a, int b) {
  return a * b;
}

int myFunc0() {
  return 0;
}

int main() {
  int a, k, u;
  char b;

  a = (3 * (5 + 1)) % 10 / 3;

  myFunc4(a, myFunc2(a, b));
  return 0;
}
