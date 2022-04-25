cmake_minimum_required(VERSION 3.21)
project(plugin)

find_package(fmt CONFIG REQUIRED)

# https://cmake.org/pipermail/cmake/2009-June/030311.html
set(CMAKE_BUILD_TYPE "Debug" CACHE STRING
    "Choose the type of build, options are: Debug Release
RelWithDebInfo MinSizeRel."
    FORCE)

set(SRCS "plugin/print.cc")

add_library(app SHARED ${SRCS})

target_link_libraries(app PRIVATE fmt::fmt)

add_custom_target(
    additional-dll ALL
    DEPENDS app
    COMMAND pwsh ../Scripts/dll.ps1
)
