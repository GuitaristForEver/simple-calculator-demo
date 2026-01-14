/**
 * Allure 3 Configuration
 * 
 * This configures the new Allure 3 report generator.
 * Docs: https://github.com/allure-framework/allure3
 */
import { defineConfig } from "allure";

export default defineConfig({
  name: "Simple Calculator - Test Report",
  output: "./allure-report",
  plugins: {
    awesome: {
      options: {
        singleFile: false,        // Generate full report (not single HTML)
        reportLanguage: "en",     // English UI
      },
    },
  },
});
