package uz.mtm.ratsion.data.local.dao

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import kotlinx.coroutines.flow.Flow
import uz.mtm.ratsion.data.local.entity.GroupEntity
import uz.mtm.ratsion.data.local.entity.GroupWithChildrenCount

@Dao
interface GroupDao {
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(group: GroupEntity)

    @Update
    suspend fun update(group: GroupEntity)

    @Delete
    suspend fun delete(group: GroupEntity)

    @Query("SELECT * FROM groups ORDER BY name")
    fun observeAll(): Flow<List<GroupEntity>>

    @Query("SELECT id, name, ageRange, childrenCount FROM groups ORDER BY name")
    suspend fun getAllWithChildrenCount(): List<GroupWithChildrenCount>
}
