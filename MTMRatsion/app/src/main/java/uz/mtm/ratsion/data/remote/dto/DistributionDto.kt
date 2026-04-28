package uz.mtm.ratsion.data.remote.dto

data class DistributionDto(
    val id: String,
    val date: String,
    val groupId: String,
    val mealType: String,
    val productId: String,
    val plannedQuantity: Double,
    val actualQuantity: Double,
    val status: String,
    val distributedBy: String,
    val notes: String
)