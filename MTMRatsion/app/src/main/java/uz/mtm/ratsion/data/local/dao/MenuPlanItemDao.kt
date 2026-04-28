package uz.mtm.ratsion.data.local.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query

import uz.mtm.ratsion.data.local.entity.MenuPlanItemEntity

@Dao
interface MenuPlanItemDao {
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertAll(items: List<MenuPlanItemEntity>)

    @Query("SELECT * FROM menu_plan_items WHERE planId = :planId ORDER BY mealType")
    suspend fun getByPlanId(planId: String): List<MenuPlanItemEntity>
}
