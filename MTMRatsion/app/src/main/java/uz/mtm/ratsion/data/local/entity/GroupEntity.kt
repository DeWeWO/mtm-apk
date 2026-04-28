package uz.mtm.ratsion.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "groups")
data class GroupEntity(
    @PrimaryKey val id: String,
    val name: String,
    val ageRange: String,
    val childrenCount: Int,
    val createdAt: Long,
    val isSynced: Boolean = false
)
