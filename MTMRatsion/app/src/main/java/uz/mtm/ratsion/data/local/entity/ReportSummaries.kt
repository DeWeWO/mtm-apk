package uz.mtm.ratsion.data.local.entity

data class DailyDistributionSummary(
    val date: String,
    val groupId: String,
    val totalPlanned: Double,
    val totalActual: Double,
    val completedCount: Int
)

data class WeeklySummary(
    val weekStart: String,
    val avgCompliance: Double,
    val totalCalories: Double
)

data class MonthlySummary(
    val month: String,
    val avgCompliance: Double,
    val totalCalories: Double
)
