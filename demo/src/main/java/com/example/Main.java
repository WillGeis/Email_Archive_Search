package com.example;

public class Main {
    public static void main(String[] args) {
        String imagePath = "C:/Users/u235211/Documents/Email_Archive_Search/W9_GF Operations LLC_10.2023.pdf";
        String result = OCRProcessor.performOCR(imagePath);
        System.out.println("OCR Result: ");
        System.out.println(result);
    }
}