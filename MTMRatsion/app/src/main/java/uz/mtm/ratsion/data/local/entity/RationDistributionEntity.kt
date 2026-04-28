package uz.mtm.ratsion.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "ration_distributions")
data class RationDistributionEntity(
    @PrimaryKey val id: String,
    val date: String,
    val groupId: String,
    val mealType: String,
    val productId: String,
    val plannedQuantity: Double,
    val actualQuantity: Double,
    val status: String,
    val distributedBy: String,
    val notes: String = "",
    val createdAt: Long,
    val isSynced: Boolean = false
)
