package uz.mtm.ratsion.data.local.dao

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import kotlinx.coroutines.flow.Flow
import uz.mtm.ratsion.data.local.entity.StockInventoryEntity

@Dao
interface InventoryDao {
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(item: StockInventoryEntity)

    @Update
    suspend fun update(item: StockInventoryEntity)

    @Delete
    suspend fun delete(item: StockInventoryEntity)

    @Query("SELECT * FROM stock_inventory WHERE productId = :productId ORDER BY createdAt DESC")
    suspend fun getMovementHistory(productId: String): List<StockInventoryEntity>

    @Query("SELECT * FROM stock_inventory ORDER BY createdAt DESC")
    fun observeAll(): Flow<List<StockInventoryEntity>>
}
