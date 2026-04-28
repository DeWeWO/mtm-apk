package uz.mtm.ratsion.presentation.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun InventoryScreen(navController: NavController) {
    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Ombor Qoldig'i", fontWeight = FontWeight.Bold) },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = MaterialTheme.colorScheme.primary, titleContentColor = Color.White)
            )
        }
    ) { paddingValues ->
        LazyColumn(
            modifier = Modifier.fillMaxSize().background(Color(0xFFF5F7FA)).padding(paddingValues).padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            item {
                InventoryItem("Kartoshka", "Sabzavotlar", "45 kg", Color.Black)
                InventoryItem("Go'sht (Mol)", "Go'sht mahsulotlari", "12 kg", Color.Black)
                InventoryItem("Guruch", "Don mahsulotlari", "2 kg", Color.Red) // Kam qolgan
            }
        }
    }
}

@Composable
fun InventoryItem(name: String, category: String, amount: String, amountColor: Color) {
    Card(shape = RoundedCornerShape(12.dp), colors = CardDefaults.cardColors(containerColor = Color.White), elevation = CardDefaults.cardElevation(1.dp)) {
        Row(modifier = Modifier.padding(16.dp).fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
            Column {
                Text(name, fontSize = 16.sp, fontWeight = FontWeight.Bold)
                Text(category, fontSize = 14.sp, color = Color.Gray)
            }
            Text(amount, fontSize = 18.sp, fontWeight = FontWeight.Bold, color = amountColor)
        }
    }
}