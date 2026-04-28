import os

base_dir = "e:/1.0/ibragimova nodira/individual loyiha/mtm-ratsion/mobile/MTMRatsion/app/src/main/java/uz/mtm/ratsion"

def write_file(path, content):
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip())

write_file("util/ConnectivityObserver.kt", """
package uz.mtm.ratsion.util

import kotlinx.coroutines.flow.Flow

interface ConnectivityObserver {
    fun observe(): Flow<Status>
    enum class Status { Available, Unavailable, Lost }
}
""")

write_file("util/NetworkConnectivityObserver.kt", """
package uz.mtm.ratsion.util

import android.content.Context
import android.net.ConnectivityManager
import android.net.Network
import kotlinx.coroutines.channels.awaitClose
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.callbackFlow
import kotlinx.coroutines.flow.distinctUntilChanged
import kotlinx.coroutines.launch

class NetworkConnectivityObserver(
    private val context: Context
) : ConnectivityObserver {

    private val connectivityManager =
        context.getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager

    override fun observe(): Flow<ConnectivityObserver.Status> {
        return callbackFlow {
            val callback = object : ConnectivityManager.NetworkCallback() {
                override fun onAvailable(network: Network) {
                    super.onAvailable(network)
                    launch { send(ConnectivityObserver.Status.Available) }
                }

                override fun onLost(network: Network) {
                    super.onLost(network)
                    launch { send(ConnectivityObserver.Status.Lost) }
                }

                override fun onUnavailable() {
                    super.onUnavailable()
                    launch { send(ConnectivityObserver.Status.Unavailable) }
                }
            }

            connectivityManager.registerDefaultNetworkCallback(callback)
            awaitClose {
                connectivityManager.unregisterNetworkCallback(callback)
            }
        }.distinctUntilChanged()
    }
}
""")

write_file("di/AppModule.kt", """
package uz.mtm.ratsion.di

import android.content.Context
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.android.qualifiers.ApplicationContext
import dagger.hilt.components.SingletonComponent
import uz.mtm.ratsion.util.ConnectivityObserver
import uz.mtm.ratsion.util.NetworkConnectivityObserver
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object AppModule {

    @Provides
    @Singleton
    fun provideConnectivityObserver(@ApplicationContext context: Context): ConnectivityObserver {
        return NetworkConnectivityObserver(context)
    }
}
""")

write_file("domain/repository/DistributionRepository.kt", """
package uz.mtm.ratsion.domain.repository

import kotlinx.coroutines.flow.Flow
import uz.mtm.ratsion.data.local.entity.RationDistributionEntity

interface DistributionRepository {
    fun getDistributionsByDateAndGroup(date: String, groupId: String): Flow<List<RationDistributionEntity>>
    suspend fun saveDistribution(distribution: RationDistributionEntity)
}
""")

write_file("data/repository/DistributionRepositoryImpl.kt", """
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
""")

write_file("di/RepositoryModule.kt", """
package uz.mtm.ratsion.di

import dagger.Binds
import dagger.Module
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import uz.mtm.ratsion.data.repository.DistributionRepositoryImpl
import uz.mtm.ratsion.domain.repository.DistributionRepository
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
abstract class RepositoryModule {

    @Binds
    @Singleton
    abstract fun bindDistributionRepository(
        distributionRepositoryImpl: DistributionRepositoryImpl
    ): DistributionRepository
}
""")

write_file("presentation/theme/Color.kt", """
package uz.mtm.ratsion.presentation.theme

import androidx.compose.ui.graphics.Color

val Primary = Color(0xFF2563EB)
val PrimaryDark = Color(0xFF1E3A5F)
val Secondary = Color(0xFF16A34A)
val Warning = Color(0xFFD97706)
val Error = Color(0xFFDC2626)
val Surface = Color(0xFFF8FAFC)
val CardBg = Color(0xFFFFFFFF)
val TextPrimary = Color(0xFF1E293B)
val TextSecondary = Color(0xFF64748B)

val NonushtaColor = Color(0xFFFF9F43)
val TushlukColor = Color(0xFF54A0FF)
val KechkiColor = Color(0xFFA29BFE)
val IkkinchiColor = Color(0xFF55EFC4)
""")

write_file("presentation/theme/Typography.kt", """
package uz.mtm.ratsion.presentation.theme

import androidx.compose.material3.Typography

val Typography = Typography()
""")

write_file("presentation/theme/Shape.kt", """
package uz.mtm.ratsion.presentation.theme

import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Shapes
import androidx.compose.ui.unit.dp

val Shapes = Shapes(
    small = RoundedCornerShape(8.dp),
    medium = RoundedCornerShape(12.dp),
    large = RoundedCornerShape(16.dp)
)
""")

write_file("presentation/theme/Theme.kt", """
package uz.mtm.ratsion.presentation.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable

private val LightColorScheme = lightColorScheme(
    primary = Primary,
    secondary = Secondary,
    error = Error,
    surface = Surface,
    background = Surface,
    onPrimary = Color.White,
    onSurface = TextPrimary
)

@Composable
fun MTMRatsionTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = LightColorScheme,
        typography = Typography,
        shapes = Shapes,
        content = content
    )
}
""")

print("gen2 complete")
