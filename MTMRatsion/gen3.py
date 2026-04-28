import os

base_dir = "e:/1.0/ibragimova nodira/individual loyiha/mtm-ratsion/mobile/MTMRatsion/app/src/main/java/uz/mtm/ratsion"

def write_file(path, content):
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip())

write_file("presentation/navigation/NavGraph.kt", """
package uz.mtm.ratsion.presentation.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import uz.mtm.ratsion.presentation.screens.*

@Composable
fun AppNavGraph() {
    val navController = rememberNavController()

    NavHost(navController = navController, startDestination = "splash") {
        composable("splash") { SplashScreen(navController) }
        composable("login") { LoginScreen(navController) }
        composable("home") { HomeScreen(navController) }
        composable("distribution") { DistributionScreen(navController) }
        composable("menu_plan") { MenuPlanScreen(navController) }
        composable("groups") { GroupsScreen(navController) }
        composable("products") { ProductsScreen(navController) }
        composable("inventory") { InventoryScreen(navController) }
        composable("reports") { ReportsScreen(navController) }
        composable("settings") { SettingsScreen(navController) }
        composable("sync") { SyncScreen(navController) }
    }
}
""")

write_file("presentation/screens/SplashScreen.kt", """
package uz.mtm.ratsion.presentation.screens

import androidx.compose.foundation.layout.*
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import kotlinx.coroutines.delay

@Composable
fun SplashScreen(navController: NavController) {
    LaunchedEffect(Unit) {
        delay(2000)
        navController.navigate("login") {
            popUpTo("splash") { inclusive = true }
        }
    }
    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        Text(text = "MTM Ratsion", fontSize = 32.sp, color = MaterialTheme.colorScheme.primary)
    }
}
""")

write_file("presentation/screens/LoginScreen.kt", """
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
""")

write_file("presentation/screens/HomeScreen.kt", """
package uz.mtm.ratsion.presentation.screens

import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController

@Composable
fun HomeScreen(navController: NavController) {
    Column(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Text(text = "Bosh Sahifa")
        Spacer(modifier = Modifier.height(16.dp))
        Button(onClick = { navController.navigate("distribution") }) {
            Text("Taqsimlash")
        }
        Button(onClick = { navController.navigate("menu_plan") }) {
            Text("Menyu Rejalashtirish")
        }
    }
}
""")

write_file("presentation/screens/DistributionScreen.kt", """
package uz.mtm.ratsion.presentation.screens

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.navigation.NavController

@Composable
fun DistributionScreen(navController: NavController) {
    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        Text(text = "Ratsion Taqsimlash")
    }
}
""")

write_file("presentation/screens/MenuPlanScreen.kt", """
package uz.mtm.ratsion.presentation.screens

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.navigation.NavController

@Composable
fun MenuPlanScreen(navController: NavController) {
    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        Text(text = "Menyu Rejalashtirish")
    }
}
""")

write_file("presentation/screens/GroupsScreen.kt", """
package uz.mtm.ratsion.presentation.screens

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.navigation.NavController

@Composable
fun GroupsScreen(navController: NavController) {
    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        Text(text = "Guruhlar")
    }
}
""")

write_file("presentation/screens/ProductsScreen.kt", """
package uz.mtm.ratsion.presentation.screens

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.navigation.NavController

@Composable
fun ProductsScreen(navController: NavController) {
    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        Text(text = "Mahsulotlar")
    }
}
""")

write_file("presentation/screens/InventoryScreen.kt", """
package uz.mtm.ratsion.presentation.screens

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.navigation.NavController

@Composable
fun InventoryScreen(navController: NavController) {
    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        Text(text = "Ombor Boshqaruvi")
    }
}
""")

write_file("presentation/screens/ReportsScreen.kt", """
package uz.mtm.ratsion.presentation.screens

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.navigation.NavController

@Composable
fun ReportsScreen(navController: NavController) {
    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        Text(text = "Hisobotlar")
    }
}
""")

write_file("presentation/screens/SettingsScreen.kt", """
package uz.mtm.ratsion.presentation.screens

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.navigation.NavController

@Composable
fun SettingsScreen(navController: NavController) {
    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        Text(text = "Sozlamalar")
    }
}
""")

write_file("presentation/screens/SyncScreen.kt", """
package uz.mtm.ratsion.presentation.screens

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.navigation.NavController

@Composable
fun SyncScreen(navController: NavController) {
    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        Text(text = "Sinxronlash")
    }
}
""")

print("gen3 complete")
