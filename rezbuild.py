# -*- coding: utf-8 -*-
import os
import sys
import shutil
import subprocess

def run_cmd(cmd, cwd=None):
    print(f"[RUN] {cmd}")
    subprocess.run(cmd, cwd=cwd, shell=True, check=True)

def clean_build_dir(path):
    if os.path.exists(path):
        print(f"🧹 Cleaning build directory (excluding build.rxt): {path}")
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if item == "build.rxt":
                print(f"🔒 Preserving {item}")
                continue
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"  🗑️  Removed directory: {item}")
            else:
                os.remove(item_path)
                print(f"  🗑️  Removed file: {item}")
    else:
        # 디렉토리가 없으면 생성
        os.makedirs(path, exist_ok=True)
        print(f"📁 Created build directory: {path}")

def clean_install_dir(path):
    if os.path.exists(path):
        print(f"🧹 Removing install directory: {path}")
        shutil.rmtree(path)

def build(source_path, build_path, install_path, targets):
    version = os.environ.get("REZ_BUILD_PROJECT_VERSION")
    src_dir = os.path.join(source_path, "source", f"vulkan-headers-{version}")
    
    # 소스 디렉토리 존재 확인
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"Source directory not found: {src_dir}")
    
    print(f"📂 Source directory: {src_dir}")
    print(f"🔨 Build directory: {build_path}")
    print(f"📦 Install directory: {install_path}")
    
    clean_build_dir(build_path)
    
    if "install" in targets:
        install_path = f"/core/Linux/APPZ/packages/vulkan_headers/{version}"
        clean_install_dir(install_path)
    
    os.chdir(build_path)
    
    # CMake 설정 (Rocky Linux 9에 최적화)
    cmake_args = [
        f"-S {src_dir}",
        "-B .",
        f"-DCMAKE_INSTALL_PREFIX={install_path}",
        "-DCMAKE_BUILD_TYPE=Release",  # 릴리스 빌드
        "-DCMAKE_POSITION_INDEPENDENT_CODE=ON",  # PIC 활성화
        "-GNinja"
    ]
    
    run_cmd("cmake " + " ".join(cmake_args))
    
    # 빌드 (병렬 처리)
    cpu_count = os.cpu_count() or 4
    run_cmd(f"ninja -j{cpu_count}")
    
    if "install" in targets:
        run_cmd("ninja install")
        
        # package.py 복사
        pkg = os.path.join(source_path, "package.py")
        dst = os.path.join(install_path, "package.py")
        if os.path.exists(pkg):
            shutil.copy(pkg, dst)
            print(f"📄 Copied package.py to {dst}")
    
    print("✅ vulkan_headers build complete.")

if __name__ == "__main__":
    try:
        build(
            source_path=os.environ["REZ_BUILD_SOURCE_PATH"],
            build_path=os.environ["REZ_BUILD_PATH"],
            install_path=os.environ["REZ_BUILD_INSTALL_PATH"],
            targets=sys.argv[1:]
        )
    except Exception as e:
        print(f"❌ Build failed: {e}")
        sys.exit(1)
