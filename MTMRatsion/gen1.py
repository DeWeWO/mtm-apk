import os

base_dir = "e:/1.0/ibragimova nodira/individual loyiha/mtm-ratsion/mobile/MTMRatsion/app/src/main/java/uz/mtm/ratsion"

def write_file(path, content):
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip())

write_file("MTMApp.kt", """
package uz.mtm.ratsion

import android.app.Application
import androidx.hilt.work.HiltWorkerFactory
import androidx.work.Configuration
import dagger.hilt.android.HiltAndroidApp
import javax.inject.Inject

@HiltAndroidApp
class MTMApp : Application(), Configuration.Provider {
    @Inject
    lateinit var workerFactory: HiltWorkerFactory

    override val workManagerConfiguration: Configuration
        get() = Configuration.Builder()
            .setWorkerFactory(workerFactory)
            .build()
}
""")

write_file("MainActivity.kt", """
package uz.mtm.ratsion

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.core.splashscreen.SplashScreen.Companion.installSplashScreen
import dagger.hilt.android.AndroidEntryPoint
import uz.mtm.ratsion.presentation.navigation.AppNavGraph
import uz.mtm.ratsion.presentation.theme.MTMRatsionTheme

@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        installSplashScreen()
        setContent {
            MTMRatsionTheme {
                AppNavGraph()
            }
        }
    }
}
""")

write_file("data/local/database/MTMDatabase.kt", """
package uz.mtm.ratsion.data.local.database

import androidx.room.Database
import androidx.room.RoomDatabase
import uz.mtm.ratsion.data.local.dao.*
import uz.mtm.ratsion.data.local.entity.*

@Database(
    entities = [
        UserEntity::class,
        GroupEntity::class,
        ProductEntity::class,
        MenuPlanEntity::class,
        MenuPlanItemEntity::class,
        RationDistributionEntity::class,
        StockInventoryEntity::class,
        NutritionalReportEntity::class,
        SyncQueueEntity::class
    ],
    version = 1,
    exportSchema = false
)
abstract class MTMDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
    abstract fun groupDao(): GroupDao
    abstract fun productDao(): ProductDao
    abstract fun menuPlanDao(): MenuPlanDao
    abstract fun menuPlanItemDao(): MenuPlanItemDao
    abstract fun distributionDao(): DistributionDao
    abstract fun inventoryDao(): InventoryDao
    abstract fun reportDao(): ReportDao
    abstract fun syncQueueDao(): SyncQueueDao
}
""")

write_file("data/local/database/DatabaseSeeder.kt", """
package uz.mtm.ratsion.data.local.database

import android.content.Context
import java.io.File

object DatabaseSeeder {
    fun getPrepopulatedDatabasePath(context: Context): String {
        return "mtm_prepopulated.db"
    }
}
""")

write_file("di/DatabaseModule.kt", """
package uz.mtm.ratsion.di

import android.content.Context
import androidx.room.Room
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.android.qualifiers.ApplicationContext
import dagger.hilt.components.SingletonComponent
import uz.mtm.ratsion.data.local.database.MTMDatabase
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object DatabaseModule {

    @Provides
    @Singleton
    fun provideMTMDatabase(@ApplicationContext context: Context): MTMDatabase {
        return Room.databaseBuilder(
            context,
            MTMDatabase::class.java,
            "mtm_database.db"
        )
        // Note: createFromAsset can be added here
        .fallbackToDestructiveMigration()
        .build()
    }

    @Provides
    fun provideUserDao(database: MTMDatabase) = database.userDao()
    @Provides
    fun provideGroupDao(database: MTMDatabase) = database.groupDao()
    @Provides
    fun provideProductDao(database: MTMDatabase) = database.productDao()
    @Provides
    fun provideMenuPlanDao(database: MTMDatabase) = database.menuPlanDao()
    @Provides
    fun provideMenuPlanItemDao(database: MTMDatabase) = database.menuPlanItemDao()
    @Provides
    fun provideDistributionDao(database: MTMDatabase) = database.distributionDao()
    @Provides
    fun provideInventoryDao(database: MTMDatabase) = database.inventoryDao()
    @Provides
    fun provideReportDao(database: MTMDatabase) = database.reportDao()
    @Provides
    fun provideSyncQueueDao(database: MTMDatabase) = database.syncQueueDao()
}
""")

write_file("di/NetworkModule.kt", """
package uz.mtm.ratsion.di

import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import okhttp3.OkHttpClient
import okhttp3.logging.HttpLoggingInterceptor
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import uz.mtm.ratsion.data.remote.api.ApiService
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {

    @Provides
    @Singleton
    fun provideOkHttpClient(): OkHttpClient {
        return OkHttpClient.Builder()
            .addInterceptor(HttpLoggingInterceptor().apply { level = HttpLoggingInterceptor.Level.BODY })
            .build()
    }

    @Provides
    @Singleton
    fun provideRetrofit(client: OkHttpClient): Retrofit {
        return Retrofit.Builder()
            .baseUrl("https://api.mtmratsion.uz/")
            .client(client)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
    }

    @Provides
    @Singleton
    fun provideApiService(retrofit: Retrofit): ApiService {
        return retrofit.create(ApiService::class.java)
    }
}
""")

write_file("data/remote/api/ApiService.kt", """
package uz.mtm.ratsion.data.remote.api

import retrofit2.Response
import retrofit2.http.*
import uz.mtm.ratsion.data.remote.dto.*

interface ApiService {
    @POST("sync/distribution")
    suspend fun createDistribution(@Body dto: DistributionDto): Response<Void>
    
    @POST("sync/group")
    suspend fun createGroup(@Body dto: GroupDto): Response<Void>
    
    // Additional endpoints for full sync
}
""")

write_file("data/remote/dto/DistributionDto.kt", """
package uz.mtm.ratsion.data.remote.dto

data class DistributionDto(
    val id: String,
    val date: String,
    val groupId: String,
    val mealType: String,
    val productId: String,
    val plannedQuantity: Double,
    val actualQuantity: Double,
    val status: String,
    val distributedBy: String,
    val notes: String
)
""")

write_file("data/remote/dto/GroupDto.kt", """
package uz.mtm.ratsion.data.remote.dto

data class GroupDto(
    val id: String,
    val name: String,
    val ageRange: String,
    val childrenCount: Int
)
""")

print("gen1 complete")
