$Env:CMAKE_PREFIX_PATH = "$PSSCriptRoot/../vcpkg/installed/x64-mingw-dynamic"

$Env:CC = "gcc"
$Env:CXX = "g++"
cmake -B $PSScriptRoot/../ninja-build -G "Ninja" -Wno-dev
