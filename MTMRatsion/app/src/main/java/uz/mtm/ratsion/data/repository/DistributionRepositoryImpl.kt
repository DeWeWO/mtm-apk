package uz.mtm.ratsion.data.repository

import com.google.gson.Gson
import kotlinx.coroutines.flow.Flow
import uz.mtm.ratsion.data.local.dao.DistributionDao
import uz.mtm.ratsion.data.local.dao.SyncQueueDao
import uz.mtm.ratsion.data.local.entity.RationDistributionEntity
import uz.mtm.ratsion.data.local.entity.SyncQueueEntity
import uz.mtm.ratsion.data.remote.api.ApiService
import uz.mtm.ratsion.data.remote.dto.DistributionDto
import uz.mtm.ratsion.domain.repository.DistributionRepository
import uz.mtm.ratsion.util.ConnectivityObserver
import javax.inject.Inject

class DistributionRepositoryImpl @Inject constructor(
    private val localDao: DistributionDao,
    private val remoteApi: ApiService,
    private val syncQueue: SyncQueueDao,
    private val connectivityObserver: ConnectivityObserver
) : DistributionRepository {

    override fun getDistributionsByDateAndGroup(date: String, groupId: String): Flow<List<RationDistributionEntity>> {
        return localDao.getByDateAndGroup(date, groupId)
    }

    override suspend fun saveDistribution(distribution: RationDistributionEntity) {
        localDao.insert(distribution)
        
        // Simulating network check for simplicity
        val isOnline = false // we would check connectivityObserver status
        if (isOnline) {
            try {
                val dto = DistributionDto(
                    id = distribution.id,
                    date = distribution.date,
                    groupId = distribution.groupId,
                    mealType = distribution.mealType,
                    productId = distribution.productId,
                    plannedQuantity = distribution.plannedQuantity,
                    actualQuantity = distribution.actualQuantity,
                    status = distribution.status,
                    distributedBy = distribution.distributedBy,
                    notes = distribution.notes
                )
                remoteApi.createDistribution(dto)
            } catch (e: Exception) {
                addToSyncQueue(distribution)
            }
        } else {
            addToSyncQueue(distribution)
        }
    }

    private suspend fun addToSyncQueue(distribution: RationDistributionEntity) {
        syncQueue.insert(
            SyncQueueEntity(
                entityType = "distribution",
                entityId = distribution.id,
                operation = "CREATE",
                payload = Gson().toJson(distribution),
                createdAt = System.currentTimeMillis()
            )
        )
    }
}