package uz.mtm.ratsion.data.local.database

import android.content.Context
import java.io.File

object DatabaseSeeder {
    fun getPrepopulatedDatabasePath(context: Context): String {
        return "mtm_prepopulated.db"
    }
}