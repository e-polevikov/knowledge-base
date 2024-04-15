

class Foo {
    int _a;
    int _b;
public:
    Foo(int a, int b) : _a(a), _b(b) {}

    int sum() {
        return _a + _b;
    }
};

int main() {
    Foo foo = Foo(20, 13);

    int x = foo.sum();

    return 0;
}
