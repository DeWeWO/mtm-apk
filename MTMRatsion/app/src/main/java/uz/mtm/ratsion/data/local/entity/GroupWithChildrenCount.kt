package uz.mtm.ratsion.data.local.entity

data class GroupWithChildrenCount(
    val id: String,
    val name: String,
    val ageRange: String,
    val childrenCount: Int
)
