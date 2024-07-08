int complexOperation(int a, int b) {
  int result;
  result = (a * b) + (a / b) - (a % b) + ((a + b) * (a - b));
  return result;
}
