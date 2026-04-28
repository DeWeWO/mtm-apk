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