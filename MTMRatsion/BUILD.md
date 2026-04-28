# MTM Ratsion — Build Yo'riqnomasi

## Talablar
- Android Studio Hedgehog (2023.1.1) yoki yangroq
- JDK 17
- Android SDK 34
- Gradle 8.2+

## Tezkor qurilish

### Debug APK (test uchun):
```bash
cd mobile/MTMRatsion
./gradlew assembleDevelopmentDebug
# APK: app/build/outputs/apk/development/debug/
```

### Release APK (tarqatish uchun):
```bash
cd mobile/MTMRatsion
./build-release.sh
# APK: build-output/MTMRatsion-v1.0.0-release.apk
```

### Qurilmaga o'rnatish:
```bash
./install-debug.sh
# Yoki USB orqali:
adb install MTMRatsion-debug.apk
```

## APK ma'lumotlari
- Package: uz.mtm.ratsion
- Min Android: 7.0 (API 24)
- Target Android: 14 (API 34)
- Arxitektura: arm64-v8a, armeabi-v7a, x86_64

## Kirish ma'lumotlari (test uchun)
| Foydalanuvchi | Parol   | Rol        |
|---------------|---------|------------|
| admin         | admin123| Admin      |
| director1     | pass123 | Direktor   |
| oshpaz1       | pass123 | Oshpaz     |
| tarbiyachi1   | pass123 | Tarbiyachi |
