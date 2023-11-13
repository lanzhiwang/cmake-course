# cmake

* https://subingwen.cn/cmake/CMake-primer/

```bash
Lindent.sh *.c
find . -name "*.c" -exec ./Lindent.sh {} \; && \
find . -name "*.h" -exec ./Lindent.sh {} \; && \
find . -name "*.c~" -exec rm -rf {} \; && \
find . -name "*.h~" -exec rm -rf {} \;

gcc -v add.c div.c main.c mult.c sub.c -o app


# 让 cmake 在编译过程中打印编印信息
# 方法1:
# 执行命令 cmake 时追加: -DCMAKE_VERBOSE_MAKEFILE=ON

cmake .. -DCMAKE_VERBOSE_MAKEFILE=ON

# 方法2:
# 在 CMakeLists.txt 中添加：set(CMAKE_VERBOSE_MAKEFILEON ON)

# 方法3:
# make 时追加: VERBOSE=1

make VERBOSE=1

cmake --build ./


```


