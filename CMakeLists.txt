cmake_minimum_required(VERSION 3.13)
project(pycpp_wrapper)

set(CMAKE_CXX_STANDARD 14)

include_directories(/opt/homebrew/opt/python@3.11/Frameworks/Python.framework/Versions/3.11/include/python3.11)

find_package(PythonLibs REQUIRED)

add_executable(pycpp_wrapper main.cpp)

target_include_directories(pycpp_wrapper PRIVATE ${PYTHON_INCLUDE_DIRS})
target_link_libraries(pycpp_wrapper PRIVATE ${PYTHON_LIBRARIES})
