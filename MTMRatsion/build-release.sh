#!/bin/bash
set -e

echo "🏗️  MTM Ratsion — Release Build boshlanmoqda..."
echo "================================================"

# Check Java version
java -version

# Clean
echo "🧹 Eski build fayllarini tozalash..."
./gradlew clean

# Lint
echo "🔍 Kod tekshiruvi..."
./gradlew lint --continue || echo "⚠️ Lint ogohlantirishlari bor, davom etilmoqda..."

# Tests
echo "🧪 Testlar ishga tushirilmoqda..."
./gradlew test

# Build debug
echo "🔨 Debug APK yasalmoqda..."
./gradlew assembleDevelopmentDebug

# Build release
echo "🚀 Release APK yasalmoqda (imzolangan)..."
./gradlew assembleProductionRelease

# Copy to output folder
mkdir -p ../../build-output
cp app/build/outputs/apk/development/debug/app-development-debug.apk \
   ../../build-output/MTMRatsion-debug.apk
cp app/build/outputs/apk/production/release/app-production-release.apk \
   ../../build-output/MTMRatsion-v1.0.0-release.apk

# Show file sizes
echo ""
echo "✅ Build muvaffaqiyatli yakunlandi!"
echo "================================================"
echo "📦 Yaratilgan fayllar:"
ls -lh ../../build-output/*.apk
echo ""
echo "📱 Debug APK o'rnatish:"
echo "   adb install ../../build-output/MTMRatsion-debug.apk"
echo ""
echo "🏪 Release APK joylashuvi:"
echo "   ../../build-output/MTMRatsion-v1.0.0-release.apk"
