# CMake generated Testfile for 
# Source directory: /home/m83/chulho/vulkan_headers/1.4.325/source/vulkan-headers-1.4.325/tests
# Build directory: /home/m83/chulho/vulkan_headers/1.4.325/build/tests
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test([=[integration.add_subdirectory]=] "/storage/.NAS5/rocky9_core/Linux/APPZ/packages/cmake/3.26.5/bin/ctest" "--build-and-test" "/home/m83/chulho/vulkan_headers/1.4.325/source/vulkan-headers-1.4.325/tests/integration" "/home/m83/chulho/vulkan_headers/1.4.325/build/tests/add_subdirectory" "--build-generator" "Ninja" "--build-options" "-DFIND_PACKAGE_TESTING=OFF" "-DVULKAN_HEADERS_ENABLE_MODULE=OFF")
set_tests_properties([=[integration.add_subdirectory]=] PROPERTIES  _BACKTRACE_TRIPLES "/home/m83/chulho/vulkan_headers/1.4.325/source/vulkan-headers-1.4.325/tests/CMakeLists.txt;10;add_test;/home/m83/chulho/vulkan_headers/1.4.325/source/vulkan-headers-1.4.325/tests/CMakeLists.txt;0;")
add_test([=[integration.install]=] "/storage/.NAS5/rocky9_core/Linux/APPZ/packages/cmake/3.26.5/bin/cmake" "--install" "/home/m83/chulho/vulkan_headers/1.4.325/build" "--prefix" "/home/m83/chulho/vulkan_headers/1.4.325/build/tests/install" "--config" "Release")
set_tests_properties([=[integration.install]=] PROPERTIES  _BACKTRACE_TRIPLES "/home/m83/chulho/vulkan_headers/1.4.325/source/vulkan-headers-1.4.325/tests/CMakeLists.txt;19;add_test;/home/m83/chulho/vulkan_headers/1.4.325/source/vulkan-headers-1.4.325/tests/CMakeLists.txt;0;")
add_test([=[integration.find_package]=] "/storage/.NAS5/rocky9_core/Linux/APPZ/packages/cmake/3.26.5/bin/ctest" "--build-and-test" "/home/m83/chulho/vulkan_headers/1.4.325/source/vulkan-headers-1.4.325/tests/integration" "/home/m83/chulho/vulkan_headers/1.4.325/build/tests/find_package" "--build-generator" "Ninja" "--build-options" "-DFIND_PACKAGE_TESTING=ON" "-DCMAKE_PREFIX_PATH=/home/m83/chulho/vulkan_headers/1.4.325/build/tests/install" "-DVULKAN_HEADERS_ENABLE_MODULE=OFF")
set_tests_properties([=[integration.find_package]=] PROPERTIES  DEPENDS "integration.install" _BACKTRACE_TRIPLES "/home/m83/chulho/vulkan_headers/1.4.325/source/vulkan-headers-1.4.325/tests/CMakeLists.txt;24;add_test;/home/m83/chulho/vulkan_headers/1.4.325/source/vulkan-headers-1.4.325/tests/CMakeLists.txt;0;")
