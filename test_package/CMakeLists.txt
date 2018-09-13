cmake_minimum_required(VERSION 2.8.12)
project(backward-package-test)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_set_find_paths()

find_package(Backward REQUIRED)
add_executable(example main.cpp)
target_link_libraries(example PRIVATE Backward::Backward)
