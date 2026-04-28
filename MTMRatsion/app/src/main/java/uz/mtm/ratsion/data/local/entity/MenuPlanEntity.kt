package uz.mtm.ratsion.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "menu_plans")
data class MenuPlanEntity(
    @PrimaryKey val id: String,
    val date: String,
    val groupId: String,
    val status: String,
    val createdAt: Long,
    val isSynced: Boolean = false
)
