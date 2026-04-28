package uz.mtm.ratsion

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.core.splashscreen.SplashScreen.Companion.installSplashScreen
import dagger.hilt.android.AndroidEntryPoint
import uz.mtm.ratsion.presentation.navigation.AppNavGraph
import uz.mtm.ratsion.presentation.theme.MTMRatsionTheme

@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        installSplashScreen()
        setContent {
            MTMRatsionTheme {
                AppNavGraph()
            }
        }
    }
}