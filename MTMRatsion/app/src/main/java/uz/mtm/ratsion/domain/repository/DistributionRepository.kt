package uz.mtm.ratsion.domain.repository

import kotlinx.coroutines.flow.Flow
import uz.mtm.ratsion.data.local.entity.RationDistributionEntity

interface DistributionRepository {
    fun getDistributionsByDateAndGroup(date: String, groupId: String): Flow<List<RationDistributionEntity>>
    suspend fun saveDistribution(distribution: RationDistributionEntity)
}