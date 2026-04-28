import os

base_dir = "e:/1.0/ibragimova nodira/individual loyiha/mtm-ratsion/mobile/MTMRatsion/app/src/main/java/uz/mtm/ratsion"

def write_file(path, content):
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip())

write_file("util/SyncWorker.kt", """
package uz.mtm.ratsion.util

import android.content.Context
import androidx.hilt.work.HiltWorker
import androidx.work.CoroutineWorker
import androidx.work.WorkerParameters
import dagger.assisted.Assisted
import dagger.assisted.AssistedInject

@HiltWorker
class SyncWorker @AssistedInject constructor(
    @Assisted context: Context,
    @Assisted params: WorkerParameters
) : CoroutineWorker(context, params) {

    override suspend fun doWork(): Result {
        return try {
            // Logic for sync all would be here
            Result.success()
        } catch (e: Exception) {
            Result.retry()
        }
    }
}
""")

write_file("util/NotificationHelper.kt", """
package uz.mtm.ratsion.util

import android.app.NotificationChannel
import android.app.NotificationManager
import android.content.Context
import android.os.Build
import androidx.core.app.NotificationCompat

class NotificationHelper(private val context: Context) {
    private val channelId = "mtm_notifications"

    init {
        createNotificationChannel()
    }

    private fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val name = "MTM Bildirishnomalari"
            val descriptionText = "Ratsion tizimidan muhim xabarlar"
            val importance = NotificationManager.IMPORTANCE_DEFAULT
            val channel = NotificationChannel(channelId, name, importance).apply {
                description = descriptionText
            }
            val notificationManager: NotificationManager =
                context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
            notificationManager.createNotificationChannel(channel)
        }
    }

    fun showNotification(title: String, message: String) {
        val builder = NotificationCompat.Builder(context, channelId)
            .setSmallIcon(android.R.drawable.ic_dialog_info)
            .setContentTitle(title)
            .setContentText(message)
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)

        val notificationManager = context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        notificationManager.notify(System.currentTimeMillis().toInt(), builder.build())
    }
}
""")

write_file("util/PdfReportGenerator.kt", """
package uz.mtm.ratsion.util

import android.content.Context
import android.os.Environment
import com.itextpdf.kernel.pdf.PdfDocument
import com.itextpdf.kernel.pdf.PdfWriter
import com.itextpdf.layout.Document
import com.itextpdf.layout.element.Paragraph
import java.io.File

class PdfReportGenerator(private val context: Context) {
    fun generateDailyReport(date: String): File? {
        return try {
            val downloadsDir = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS)
            val file = File(downloadsDir, "Kunlik_Hisobot_$date.pdf")
            val writer = PdfWriter(file)
            val pdf = PdfDocument(writer)
            val document = Document(pdf)

            document.add(Paragraph("MTM Kunlik Ratsion Hisoboti"))
            document.add(Paragraph("Sana: $date"))
            // Further PDF generation logic...

            document.close()
            file
        } catch (e: Exception) {
            null
        }
    }
}
""")

print("gen4 complete")
