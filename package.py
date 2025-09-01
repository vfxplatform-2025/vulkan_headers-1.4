# -*- coding: utf-8 -*-
name = "vulkan_headers"
version = "1.4.325"
authors = ["Khronos Group"]
description = "Vulkan Headers for Vulkan SDK (rez packaged)"

# 빌드 의존성
build_requires = ["cmake", "ninja"]

# 빌드 명령
build_command = 'python {root}/rezbuild.py {install}'

# 런타임 의존성 (다른 패키지에서 vulkan_headers를 참조할 때)
requires = []

# 패키지 변형 (필요시)
variants = []

def commands():
    """환경변수 설정"""
    
    # CMake가 vulkan-headers를 찾을 수 있도록
    env.CMAKE_PREFIX_PATH.append("{root}")
    env.CMAKE_PREFIX_PATH.append("{root}/share/cmake")
    
    # 헤더 파일 경로
    env.CPATH.append("{root}/include")
    env.C_INCLUDE_PATH.append("{root}/include")
    env.CPLUS_INCLUDE_PATH.append("{root}/include")
    
    # Vulkan SDK 관련 환경변수
    env.VULKAN_SDK = "{root}"
    env.VK_LAYER_PATH.append("{root}/share/vulkan/explicit_layer.d")
