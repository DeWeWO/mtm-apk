package uz.mtm.ratsion.data.local.dao

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import kotlinx.coroutines.flow.Flow
import uz.mtm.ratsion.data.local.entity.DailyDistributionSummary
import uz.mtm.ratsion.data.local.entity.RationDistributionEntity

@Dao
interface DistributionDao {
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(item: RationDistributionEntity)

    @Update
    suspend fun update(item: RationDistributionEntity)

    @Delete
    suspend fun delete(item: RationDistributionEntity)

    @Query("SELECT * FROM ration_distributions WHERE date = :date AND groupId = :groupId ORDER BY mealType")
    fun getByDateAndGroup(date: String, groupId: String): Flow<List<RationDistributionEntity>>

    @Query(
        "SELECT date as date, groupId as groupId, SUM(plannedQuantity) as totalPlanned, " +
            "SUM(actualQuantity) as totalActual, " +
            "SUM(CASE WHEN status = 'Berildi' THEN 1 ELSE 0 END) as completedCount " +
            "FROM ration_distributions WHERE date = :date AND groupId = :groupId"
    )
    suspend fun getDailySummary(date: String, groupId: String): DailyDistributionSummary?

    @Query("SELECT * FROM ration_distributions WHERE isSynced = 0 ORDER BY createdAt")
    suspend fun getUnsyncedRecords(): List<RationDistributionEntity>

    @Query("SELECT * FROM ration_distributions ORDER BY date DESC")
    fun observeAll(): Flow<List<RationDistributionEntity>>
}
