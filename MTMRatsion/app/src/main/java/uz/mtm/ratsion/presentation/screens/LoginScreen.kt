package uz.mtm.ratsion.presentation.screens

import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController

@Composable
fun LoginScreen(navController: NavController) {
    var username by remember { mutableStateOf("") }
    var password by remember { mutableStateOf("") }

    Column(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Text(text = "Tizimga kirish")
        Spacer(modifier = Modifier.height(16.dp))
        OutlinedTextField(
            value = username,
            onValueChange = { username = it },
            label = { Text("Foydalanuvchi nomi") }
        )
        Spacer(modifier = Modifier.height(8.dp))
        OutlinedTextField(
            value = password,
            onValueChange = { password = it },
            label = { Text("Parol") }
        )
        Spacer(modifier = Modifier.height(16.dp))
        Button(onClick = { navController.navigate("home") }) {
            Text("Kirish")
        }
    }
}