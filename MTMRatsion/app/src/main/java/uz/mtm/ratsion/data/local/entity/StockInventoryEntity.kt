package uz.mtm.ratsion.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "stock_inventory")
data class StockInventoryEntity(
    @PrimaryKey val id: String,
    val productId: String,
    val movementType: String,
    val quantity: Double,
    val notes: String,
    val createdAt: Long,
    val isSynced: Boolean = false
)
