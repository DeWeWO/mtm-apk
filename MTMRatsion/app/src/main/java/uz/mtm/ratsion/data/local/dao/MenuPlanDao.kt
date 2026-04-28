package uz.mtm.ratsion.data.local.dao

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import kotlinx.coroutines.flow.Flow
import uz.mtm.ratsion.data.local.entity.MenuPlanEntity

@Dao
interface MenuPlanDao {
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(plan: MenuPlanEntity)

    @Update
    suspend fun update(plan: MenuPlanEntity)

    @Delete
    suspend fun delete(plan: MenuPlanEntity)

    @Query("SELECT * FROM menu_plans WHERE date = :date AND groupId = :groupId LIMIT 1")
    suspend fun getByDateAndGroup(date: String, groupId: String): MenuPlanEntity?

    @Query("SELECT * FROM menu_plans WHERE date BETWEEN :startDate AND :endDate ORDER BY date")
    suspend fun getByDateRange(startDate: String, endDate: String): List<MenuPlanEntity>

    @Query("SELECT * FROM menu_plans ORDER BY date DESC")
    fun observeAll(): Flow<List<MenuPlanEntity>>
}
