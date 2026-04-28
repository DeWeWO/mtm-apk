package uz.mtm.ratsion.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "menu_plan_items")
data class MenuPlanItemEntity(
    @PrimaryKey val id: String,
    val planId: String,
    val productId: String,
    val mealType: String,
    val quantity: Double,
    val calories: Double,
    val protein: Double,
    val fat: Double,
    val carbs: Double
)
