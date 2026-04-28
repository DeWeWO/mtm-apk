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