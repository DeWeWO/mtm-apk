package uz.mtm.ratsion.data.local.dao

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import uz.mtm.ratsion.data.local.entity.SyncQueueEntity

@Dao
interface SyncQueueDao {
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(item: SyncQueueEntity)

    @Query("SELECT * FROM sync_queue ORDER BY createdAt ASC")
    suspend fun getPendingItems(): List<SyncQueueEntity>

    @Query("UPDATE sync_queue SET retryCount = retryCount + 1 WHERE id = :id")
    suspend fun incrementRetry(id: Int)

    @Delete
    suspend fun delete(item: SyncQueueEntity)

    @Query("DELETE FROM sync_queue WHERE retryCount >= :maxRetries")
    suspend fun deleteCompleted(maxRetries: Int = 3)
}
