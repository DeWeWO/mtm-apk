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