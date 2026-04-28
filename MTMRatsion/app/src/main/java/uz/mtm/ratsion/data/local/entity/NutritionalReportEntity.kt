package uz.mtm.ratsion.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "nutritional_reports")
data class NutritionalReportEntity(
    @PrimaryKey val id: String,
    val date: String,
    val groupId: String,
    val totalCalories: Double,
    val totalProtein: Double,
    val totalFat: Double,
    val totalCarbs: Double,
    val compliancePercent: Double,
    val createdAt: Long,
    val isSynced: Boolean = false
)
