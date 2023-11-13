cmake_minimum_required(VERSION 3.0)
project(CALC)

set(CMAKE_VERBOSE_MAKEFILEON ON)

message(STATUS "PROJECT_SOURCE_DIR path: ${PROJECT_SOURCE_DIR}")
message(STATUS "CMAKE_CURRENT_SOURCE_DIR path: ${CMAKE_CURRENT_SOURCE_DIR}")

# 增加 -std=c++11
# set(CMAKE_CXX_STANDARD 11)
# 增加 -std=c++14
# set(CMAKE_CXX_STANDARD 14)
# 增加 -std=c++17
# set(CMAKE_CXX_STANDARD 17)

# 指定输出的路径
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

# set(SRC_LIST add.c div.c main.c mult.c sub.c)
# set(SRC_LIST add.c;div.c;main.c;mult.c;sub.c)

include_directories(${PROJECT_SOURCE_DIR}/include)

# 搜索 src 目录下的源文件
# aux_source_directory(${PROJECT_SOURCE_DIR}/src SRC_LIST)
file(GLOB SRC_LIST ${PROJECT_SOURCE_DIR}/src/*.c)

add_executable(app ${SRC_LIST})
