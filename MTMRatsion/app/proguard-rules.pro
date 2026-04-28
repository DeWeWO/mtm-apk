# Keep app models
-keep class uz.mtm.ratsion.data.** { *; }
-keep class uz.mtm.ratsion.domain.model.** { *; }

# Room
-keep class * extends androidx.room.RoomDatabase
-keep @androidx.room.Entity class *
-keepclassmembers class * extends androidx.room.RoomDatabase {
    abstract ** *Dao();
}

# Retrofit + Gson
-keepattributes Signature
-keepattributes *Annotation*
-keep class retrofit2.** { *; }
-keep class com.google.gson.** { *; }
-keepclassmembers,allowobfuscation class * {
    @com.google.gson.annotations.SerializedName <fields>;
}

# Hilt
-keep class dagger.hilt.** { *; }
-keep class javax.inject.** { *; }
-keep @dagger.hilt.android.HiltAndroidApp class *

# Kotlin Coroutines
-keepnames class kotlinx.coroutines.internal.MainDispatcherFactory {}
-keepnames class kotlinx.coroutines.CoroutineExceptionHandler {}

# Compose
-keep class androidx.compose.** { *; }

# WorkManager
-keep class * extends androidx.work.Worker
-keep class * extends androidx.work.ListenableWorker

# Keep R classes
-keepclassmembers class **.R$* {
    public static <fields>;
}

# Remove logging in release
-assumenosideeffects class android.util.Log {
    public static boolean isLoggable(java.lang.String, int);
    public static int v(...);
    public static int d(...);
    public static int i(...);
}
