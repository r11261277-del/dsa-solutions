class Solution {

    // Capitalizes the first and last character of each word in a string
    public String capitalizeFirstLast(String s) {
        // Split the string into words
        String[] words = s.split(" ");

        // StringBuilder for the result
        StringBuilder result = new StringBuilder();

        // Process each word
        for (String word : words) {
            // Capitalize single-character words
            if (word.length() == 1) {
                word = word.toUpperCase();
            } else {
                // Capitalize first and last character
                word = word.substring(0, 1).toUpperCase() +
                       word.substring(1, word.length() - 1) +
                       word.substring(word.length() - 1).toUpperCase();