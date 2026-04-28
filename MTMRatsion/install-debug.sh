#!/bin/bash
echo "📱 Debug APK qurilmaga o'rnatilmoqda..."
adb devices
adb install -r app/build/outputs/apk/development/debug/app-development-debug.apk
echo "✅ O'rnatish yakunlandi! Ilovani qurilmangizda oching."
adb shell am start -n uz.mtm.ratsion.dev/.presentation.MainActivity
