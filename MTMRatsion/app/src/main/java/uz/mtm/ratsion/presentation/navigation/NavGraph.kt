package uz.mtm.ratsion.presentation.navigation

import androidx.compose.foundation.layout.padding
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.navigation.NavController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.currentBackStackEntryAsState
import androidx.navigation.compose.rememberNavController
import uz.mtm.ratsion.presentation.screens.*

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AppNavGraph() {
    val navController = rememberNavController()
    val navBackStackEntry by navController.currentBackStackEntryAsState()
    val currentRoute = navBackStackEntry?.destination?.route
    
    val showBottomBar = currentRoute in listOf("home", "distribution", "menu_plan", "inventory", "settings")

    Scaffold(
        bottomBar = {
            if (showBottomBar) {
                NavigationBar(containerColor = MaterialTheme.colorScheme.surfaceVariant) {
                    NavigationBarItem(
                        icon = { Icon(Icons.Default.Home, contentDescription = "Asosiy") },
                        label = { Text("Asosiy") },
                        selected = currentRoute == "home",
                        onClick = { navController.navigate("home") { launchSingleTop = true; restoreState = true } }
                    )
                    NavigationBarItem(
                        icon = { Icon(Icons.Default.RestaurantMenu, contentDescription = "Menyu") },
                        label = { Text("Menyu") },
                        selected = currentRoute == "menu_plan",
                        onClick = { navController.navigate("menu_plan") { launchSingleTop = true; restoreState = true } }
                    )
                    NavigationBarItem(
                        icon = { Icon(Icons.Default.CheckCircle, contentDescription = "Taqsimot") },
                        label = { Text("Taqsimot") },
                        selected = currentRoute == "distribution",
                        onClick = { navController.navigate("distribution") { launchSingleTop = true; restoreState = true } }
                    )
                    NavigationBarItem(
                        icon = { Icon(Icons.Default.Settings, contentDescription = "Sozlamalar") },
                        label = { Text("Sozlamalar") },
                        selected = currentRoute == "settings",
                        onClick = { navController.navigate("settings") { launchSingleTop = true; restoreState = true } }
                    )
                }
            }
        }
    ) { innerPadding ->
        NavHost(
            navController = navController,
            startDestination = "splash",
            modifier = Modifier.padding(innerPadding)
        ) {
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
}