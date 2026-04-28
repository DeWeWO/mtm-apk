package uz.mtm.ratsion.data.local.dao

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import kotlinx.coroutines.flow.Flow
import uz.mtm.ratsion.data.local.entity.ProductEntity

@Dao
interface ProductDao {
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(product: ProductEntity)

    @Update
    suspend fun update(product: ProductEntity)

    @Delete
    suspend fun delete(product: ProductEntity)

    @Query("SELECT * FROM products ORDER BY name")
    fun observeAll(): Flow<List<ProductEntity>>

    @Query("SELECT * FROM products WHERE category = :category ORDER BY name")
    suspend fun findByCategory(category: String): List<ProductEntity>

    @Query("SELECT * FROM products WHERE currentStock <= minStockLevel ORDER BY currentStock ASC")
    suspend fun getLowStockProducts(): List<ProductEntity>

    @Query("SELECT * FROM products WHERE name LIKE '%' || :query || '%' ORDER BY name")
    suspend fun searchByName(query: String): List<ProductEntity>
}
