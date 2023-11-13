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

## build 详细过程

```bash
root@2b58dd9be00e:/cmake-course/v4/dist# make VERBOSE=1
/usr/bin/cmake -S/cmake-course/v4 -B/cmake-course/v4/dist --check-build-system CMakeFiles/Makefile.cmake 0
/usr/bin/cmake -E cmake_progress_start /cmake-course/v4/dist/CMakeFiles /cmake-course/v4/dist//CMakeFiles/progress.marks
make  -f CMakeFiles/Makefile2 all
make[1]: Entering directory '/cmake-course/v4/dist'
make  -f CMakeFiles/calc_shared.dir/build.make CMakeFiles/calc_shared.dir/depend
make[2]: Entering directory '/cmake-course/v4/dist'
cd /cmake-course/v4/dist && /usr/bin/cmake -E cmake_depends "Unix Makefiles" /cmake-course/v4 /cmake-course/v4 /cmake-course/v4/dist /cmake-course/v4/dist /cmake-course/v4/dist/CMakeFiles/calc_shared.dir/DependInfo.cmake --color=
Dependee "/cmake-course/v4/dist/CMakeFiles/calc_shared.dir/DependInfo.cmake" is newer than depender "/cmake-course/v4/dist/CMakeFiles/calc_shared.dir/depend.internal".
Dependee "/cmake-course/v4/dist/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/cmake-course/v4/dist/CMakeFiles/calc_shared.dir/depend.internal".
Scanning dependencies of target calc_shared
make[2]: Leaving directory '/cmake-course/v4/dist'
make  -f CMakeFiles/calc_shared.dir/build.make CMakeFiles/calc_shared.dir/build
make[2]: Entering directory '/cmake-course/v4/dist'
[  7%] Building C object CMakeFiles/calc_shared.dir/src/add.c.o
/usr/bin/cc -Dcalc_shared_EXPORTS -I/cmake-course/v4/include -fPIC -o CMakeFiles/calc_shared.dir/src/add.c.o -c /cmake-course/v4/src/add.c
[ 14%] Building C object CMakeFiles/calc_shared.dir/src/div.c.o
/usr/bin/cc -Dcalc_shared_EXPORTS -I/cmake-course/v4/include -fPIC -o CMakeFiles/calc_shared.dir/src/div.c.o -c /cmake-course/v4/src/div.c
[ 21%] Building C object CMakeFiles/calc_shared.dir/src/mult.c.o
/usr/bin/cc -Dcalc_shared_EXPORTS -I/cmake-course/v4/include -fPIC -o CMakeFiles/calc_shared.dir/src/mult.c.o -c /cmake-course/v4/src/mult.c
[ 28%] Building C object CMakeFiles/calc_shared.dir/src/sub.c.o
/usr/bin/cc -Dcalc_shared_EXPORTS -I/cmake-course/v4/include -fPIC -o CMakeFiles/calc_shared.dir/src/sub.c.o -c /cmake-course/v4/src/sub.c
[ 35%] Linking C shared library ../lib/libcalc_shared.so
/usr/bin/cmake -E cmake_link_script CMakeFiles/calc_shared.dir/link.txt --verbose=1
/usr/bin/cc -fPIC -shared -Wl,-soname,libcalc_shared.so -o ../lib/libcalc_shared.so CMakeFiles/calc_shared.dir/src/add.c.o CMakeFiles/calc_shared.dir/src/div.c.o CMakeFiles/calc_shared.dir/src/mult.c.o CMakeFiles/calc_shared.dir/src/sub.c.o
make[2]: Leaving directory '/cmake-course/v4/dist'
[ 35%] Built target calc_shared
make  -f CMakeFiles/calc_static.dir/build.make CMakeFiles/calc_static.dir/depend
make[2]: Entering directory '/cmake-course/v4/dist'
cd /cmake-course/v4/dist && /usr/bin/cmake -E cmake_depends "Unix Makefiles" /cmake-course/v4 /cmake-course/v4 /cmake-course/v4/dist /cmake-course/v4/dist /cmake-course/v4/dist/CMakeFiles/calc_static.dir/DependInfo.cmake --color=
Dependee "/cmake-course/v4/dist/CMakeFiles/calc_static.dir/DependInfo.cmake" is newer than depender "/cmake-course/v4/dist/CMakeFiles/calc_static.dir/depend.internal".
Dependee "/cmake-course/v4/dist/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/cmake-course/v4/dist/CMakeFiles/calc_static.dir/depend.internal".
Scanning dependencies of target calc_static
make[2]: Leaving directory '/cmake-course/v4/dist'
make  -f CMakeFiles/calc_static.dir/build.make CMakeFiles/calc_static.dir/build
make[2]: Entering directory '/cmake-course/v4/dist'
[ 42%] Building C object CMakeFiles/calc_static.dir/src/add.c.o
/usr/bin/cc  -I/cmake-course/v4/include  -o CMakeFiles/calc_static.dir/src/add.c.o -c /cmake-course/v4/src/add.c
[ 50%] Building C object CMakeFiles/calc_static.dir/src/div.c.o
/usr/bin/cc  -I/cmake-course/v4/include  -o CMakeFiles/calc_static.dir/src/div.c.o -c /cmake-course/v4/src/div.c
[ 57%] Building C object CMakeFiles/calc_static.dir/src/mult.c.o
/usr/bin/cc  -I/cmake-course/v4/include  -o CMakeFiles/calc_static.dir/src/mult.c.o -c /cmake-course/v4/src/mult.c
[ 64%] Building C object CMakeFiles/calc_static.dir/src/sub.c.o
/usr/bin/cc  -I/cmake-course/v4/include  -o CMakeFiles/calc_static.dir/src/sub.c.o -c /cmake-course/v4/src/sub.c
[ 71%] Linking C static library ../lib/libcalc_static.a
/usr/bin/cmake -P CMakeFiles/calc_static.dir/cmake_clean_target.cmake
/usr/bin/cmake -E cmake_link_script CMakeFiles/calc_static.dir/link.txt --verbose=1
/usr/bin/ar qc ../lib/libcalc_static.a CMakeFiles/calc_static.dir/src/add.c.o CMakeFiles/calc_static.dir/src/div.c.o CMakeFiles/calc_static.dir/src/mult.c.o CMakeFiles/calc_static.dir/src/sub.c.o
/usr/bin/ranlib ../lib/libcalc_static.a
make[2]: Leaving directory '/cmake-course/v4/dist'
[ 71%] Built target calc_static
make  -f CMakeFiles/app_shared.dir/build.make CMakeFiles/app_shared.dir/depend
make[2]: Entering directory '/cmake-course/v4/dist'
cd /cmake-course/v4/dist && /usr/bin/cmake -E cmake_depends "Unix Makefiles" /cmake-course/v4 /cmake-course/v4 /cmake-course/v4/dist /cmake-course/v4/dist /cmake-course/v4/dist/CMakeFiles/app_shared.dir/DependInfo.cmake --color=
Dependee "/cmake-course/v4/dist/CMakeFiles/app_shared.dir/DependInfo.cmake" is newer than depender "/cmake-course/v4/dist/CMakeFiles/app_shared.dir/depend.internal".
Dependee "/cmake-course/v4/dist/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/cmake-course/v4/dist/CMakeFiles/app_shared.dir/depend.internal".
Scanning dependencies of target app_shared
make[2]: Leaving directory '/cmake-course/v4/dist'
make  -f CMakeFiles/app_shared.dir/build.make CMakeFiles/app_shared.dir/build
make[2]: Entering directory '/cmake-course/v4/dist'
[ 78%] Building C object CMakeFiles/app_shared.dir/main.c.o
/usr/bin/cc  -I/cmake-course/v4/include  -o CMakeFiles/app_shared.dir/main.c.o -c /cmake-course/v4/main.c
[ 85%] Linking C executable ../bin/app_shared
/usr/bin/cmake -E cmake_link_script CMakeFiles/app_shared.dir/link.txt --verbose=1
/usr/bin/cc -rdynamic CMakeFiles/app_shared.dir/main.c.o -o ../bin/app_shared   -L/cmake-course/v4/lib  -Wl,-rpath,/cmake-course/v4/lib ../lib/libcalc_static.a ../lib/libcalc_shared.so -lpthread
make[2]: Leaving directory '/cmake-course/v4/dist'
[ 85%] Built target app_shared
make  -f CMakeFiles/app_static.dir/build.make CMakeFiles/app_static.dir/depend
make[2]: Entering directory '/cmake-course/v4/dist'
cd /cmake-course/v4/dist && /usr/bin/cmake -E cmake_depends "Unix Makefiles" /cmake-course/v4 /cmake-course/v4 /cmake-course/v4/dist /cmake-course/v4/dist /cmake-course/v4/dist/CMakeFiles/app_static.dir/DependInfo.cmake --color=
Dependee "/cmake-course/v4/dist/CMakeFiles/app_static.dir/DependInfo.cmake" is newer than depender "/cmake-course/v4/dist/CMakeFiles/app_static.dir/depend.internal".
Dependee "/cmake-course/v4/dist/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/cmake-course/v4/dist/CMakeFiles/app_static.dir/depend.internal".
Scanning dependencies of target app_static
make[2]: Leaving directory '/cmake-course/v4/dist'
make  -f CMakeFiles/app_static.dir/build.make CMakeFiles/app_static.dir/build
make[2]: Entering directory '/cmake-course/v4/dist'
[ 92%] Building C object CMakeFiles/app_static.dir/main.c.o
/usr/bin/cc  -I/cmake-course/v4/include  -o CMakeFiles/app_static.dir/main.c.o -c /cmake-course/v4/main.c
[100%] Linking C executable ../bin/app_static
/usr/bin/cmake -E cmake_link_script CMakeFiles/app_static.dir/link.txt --verbose=1
/usr/bin/cc -rdynamic CMakeFiles/app_static.dir/main.c.o -o ../bin/app_static   -L/cmake-course/v4/lib  -Wl,-rpath,/cmake-course/v4/lib ../lib/libcalc_static.a
make[2]: Leaving directory '/cmake-course/v4/dist'
[100%] Built target app_static
make[1]: Leaving directory '/cmake-course/v4/dist'
/usr/bin/cmake -E cmake_progress_start /cmake-course/v4/dist/CMakeFiles 0
root@2b58dd9be00e:/cmake-course/v4/dist#

```
