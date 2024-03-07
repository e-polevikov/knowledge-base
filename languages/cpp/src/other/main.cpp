#include <iostream>

/*
int foo();

int bar() {
  return foo();
} */

extern int x;

int main() {
  /*
  std::cout << sizeof(int) << std::endl;
  std::cout << sizeof(int*) << std::endl; */

  //int a[2000000];

  //a[0] = 42;

  std::cout << sizeof(char*) << std::endl;

  std::cout << x << std::endl;

  return 0;
}
