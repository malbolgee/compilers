char myFunc0() {
  return 0;
}

int myFunc1(int a, int b) {
  return a + b;
}

int main() {

  myFunc1(myFunc0(), 1 + 1);

  return 0;
}
