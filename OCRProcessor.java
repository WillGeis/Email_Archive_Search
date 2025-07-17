import net.sourceforge.tess4j.ITesseract;
import net.sourceforge.tess4j.Tesseract;
import net.sourceforge.tess4j.TesseractException;

import java.io.File;

public class OCRProcessor {

    public static String performOCR(String imagePath) {
        ITesseract instance = new Tesseract();

        // Set the path to the tessdata directory
        instance.setDatapath("C:/Program Files/Tesseract-OCR/tessdata");

        try {
            // Perform OCR on the image file
            String result = instance.doOCR(new File(imagePath));
            return result;
        } catch (TesseractException e) {
            e.printStackTrace();
            return "Error: " + e.getMessage();
        }
    }

    public static void main(String[] args) {
        String imagePath = "path/to/your/image/file.png";
        String result = performOCR(imagePath);
        System.out.println("OCR Result: ");
        System.out.println(result);
    }
}
