#include <fmt/core.h>

extern "C"
{
    void print_hello();
}

void print_hello()
{
    fmt::print("hello from fmt\n");
}