cmake_minimum_required(VERSION 3.0)
project(CALC)

set(CMAKE_VERBOSE_MAKEFILEON ON)

message(STATUS "PROJECT_SOURCE_DIR path: ${PROJECT_SOURCE_DIR}")
message(STATUS "CMAKE_CURRENT_SOURCE_DIR path: ${CMAKE_CURRENT_SOURCE_DIR}")

# 指定输出的路径
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

include_directories(${PROJECT_SOURCE_DIR}/include)

file(GLOB SRC_LIST ${PROJECT_SOURCE_DIR}/src/*.c)

# 设置动态库/静态库生成路径
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

# 生成动态库
add_library(calc_shared SHARED ${SRC_LIST})
# 生成静态库
add_library(calc_static STATIC ${SRC_LIST})

# 库路径
link_directories(${PROJECT_SOURCE_DIR}/lib)
# 链接静态库
link_libraries(calc_static)
add_executable(app_static main.c)

add_executable(app_shared main.c)
# 链接动态库
target_link_libraries(app_shared calc_shared)
target_link_libraries(app_shared pthread)
