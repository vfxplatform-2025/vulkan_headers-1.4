#!/bin/bash
set -e

VERSION=1.4.325
TAG=sdk-${VERSION}
PKG_NAME=vulkan-headers
SRC_DIR=$(pwd)/source
TARGET_DIR=${SRC_DIR}/${PKG_NAME}-${VERSION}

if [ -d "$TARGET_DIR" ]; then
    echo "✅ Source already exists: $TARGET_DIR"
    exit 0
fi

echo "⬇️  Cloning ${PKG_NAME}-${VERSION} (tag: ${TAG})..."

mkdir -p "$SRC_DIR"
cd "$SRC_DIR"

git clone https://github.com/KhronosGroup/Vulkan-Headers.git ${PKG_NAME}-${VERSION}
cd ${PKG_NAME}-${VERSION}

# ✅ 정확한 태그 checkout
git checkout tags/${TAG} -b build-${VERSION}

echo "✅ Done: $TARGET_DIR"

