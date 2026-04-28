package uz.mtm.ratsion.data.local.dao

import androidx.room.Dao
import androidx.room.Query
import uz.mtm.ratsion.data.local.entity.MonthlySummary
import uz.mtm.ratsion.data.local.entity.NutritionalReportEntity
import uz.mtm.ratsion.data.local.entity.WeeklySummary

@Dao
interface ReportDao {
    @androidx.room.Insert(onConflict = androidx.room.OnConflictStrategy.REPLACE)
    suspend fun insert(report: NutritionalReportEntity)

    @Query("SELECT * FROM nutritional_reports WHERE date = :date AND groupId = :groupId LIMIT 1")
    suspend fun getNutritionalReport(date: String, groupId: String): NutritionalReportEntity?

    @Query(
        "SELECT substr(date, 1, 7) as weekStart, AVG(compliancePercent) as avgCompliance, " +
            "SUM(totalCalories) as totalCalories FROM nutritional_reports " +
            "WHERE date BETWEEN :startDate AND :endDate"
    )
    suspend fun getWeeklySummary(startDate: String, endDate: String): WeeklySummary?

    @Query(
        "SELECT substr(date, 1, 7) as month, AVG(compliancePercent) as avgCompliance, " +
            "SUM(totalCalories) as totalCalories FROM nutritional_reports " +
            "WHERE date BETWEEN :startDate AND :endDate"
    )
    suspend fun getMonthlySummary(startDate: String, endDate: String): MonthlySummary?
}
