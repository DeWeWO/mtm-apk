package uz.mtm.ratsion.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "products")
data class ProductEntity(
    @PrimaryKey val id: String,
    val name: String,
    val category: String,
    val unit: String,
    val caloriesPerUnit: Double,
    val protein: Double,
    val fat: Double,
    val carbs: Double,
    val currentStock: Double = 0.0,
    val minStockLevel: Double = 5.0,
    val isSynced: Boolean = false
)
