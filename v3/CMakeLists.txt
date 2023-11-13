cmake_minimum_required(VERSION 3.0)
project(CALC)

set(CMAKE_VERBOSE_MAKEFILEON ON)

message(STATUS "PROJECT_SOURCE_DIR path: ${PROJECT_SOURCE_DIR}")
message(STATUS "CMAKE_CURRENT_SOURCE_DIR path: ${CMAKE_CURRENT_SOURCE_DIR}")

include_directories(${PROJECT_SOURCE_DIR}/include)

file(GLOB SRC_LIST ${PROJECT_SOURCE_DIR}/src/*.c)

# 设置动态库/静态库生成路径
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

# 生成动态库
add_library(calc_shared SHARED ${SRC_LIST})
# 生成静态库
add_library(calc_static STATIC ${SRC_LIST})
