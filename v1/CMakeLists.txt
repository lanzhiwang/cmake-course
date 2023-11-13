cmake_minimum_required(VERSION 3.0)
project(CALC)

set(CMAKE_VERBOSE_MAKEFILEON ON)

message(STATUS "source path: ${PROJECT_SOURCE_DIR}")
message(STATUS "source path: ${CMAKE_CURRENT_SOURCE_DIR}")

add_executable(app add.c div.c main.c mult.c sub.c)
