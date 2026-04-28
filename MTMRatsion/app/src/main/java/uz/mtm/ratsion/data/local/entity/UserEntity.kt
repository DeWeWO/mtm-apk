package uz.mtm.ratsion.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "users")
data class UserEntity(
    @PrimaryKey val id: String,
    val fullName: String,
    val username: String,
    val passwordHash: String,
    val role: String,
    val groupId: String?,
    val createdAt: Long,
    val isSynced: Boolean = false
)
