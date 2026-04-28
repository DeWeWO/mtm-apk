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