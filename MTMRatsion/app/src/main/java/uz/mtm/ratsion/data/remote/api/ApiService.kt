package uz.mtm.ratsion.data.remote.api

import retrofit2.Response
import retrofit2.http.*
import uz.mtm.ratsion.data.remote.dto.*

interface ApiService {
    @POST("sync/distribution")
    suspend fun createDistribution(@Body dto: DistributionDto): Response<Void>
    
    @POST("sync/group")
    suspend fun createGroup(@Body dto: GroupDto): Response<Void>
    
    // Additional endpoints for full sync
}