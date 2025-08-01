package com.example;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

import org.apache.pdfbox.Loader;
import org.apache.pdfbox.io.RandomAccessReadBufferedFile;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.rendering.PDFRenderer;

import net.sourceforge.tess4j.ITesseract;
import net.sourceforge.tess4j.Tesseract;
import net.sourceforge.tess4j.TesseractException;

public class OCRProcessor {

    public static String performOCR(String pdfPath) {
        ITesseract tesseract = new Tesseract(); // Ensure proper instantiation
        StringBuilder extractedText = new StringBuilder();

        try (PDDocument document = Loader.loadPDF(new RandomAccessReadBufferedFile(new File(pdfPath)))) {
            PDFRenderer pdfRenderer = new PDFRenderer(document);
            for (int page = 0; page < document.getNumberOfPages(); ++page) {
                BufferedImage image = pdfRenderer.renderImageWithDPI(page, 300);
                File tempImageFile = new File("temp_page_" + page + ".png");
                ImageIO.write(image, "png", tempImageFile);

                try {
                    String result = tesseract.doOCR(tempImageFile);
                    extractedText.append(result);
                } catch (TesseractException e) {
                    extractedText.append("Error on page ").append(page).append(": ").append(e.getMessage());
                }

                tempImageFile.delete();
            }
        } catch (IOException e) {
            return "Failed to process PDF: " + e.getMessage();
        }

        return extractedText.toString();
    }
}


