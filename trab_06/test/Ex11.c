int myFunc(int a, int b) {
  if (a == 0) {
    return (a * b) + a;
  } else {
    while (a > 0) {
      --a;
      b += a;
    }
  }
  return b;
}

int main() {
  int a;
  int b;

  while (a < b) {
    if (a % b == 0) {
      a = (b + a) / (++b);
      a = myFunc(a, b);
    } else {
      b = (a - b) * (++a);
      b = myFunc(b, a);
    }
  }
  return a % b;
}
