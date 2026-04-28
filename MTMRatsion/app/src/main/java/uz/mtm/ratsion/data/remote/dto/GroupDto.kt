package uz.mtm.ratsion.data.remote.dto

data class GroupDto(
    val id: String,
    val name: String,
    val ageRange: String,
    val childrenCount: Int
)