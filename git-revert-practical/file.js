// app.js
// Simple temporary Node.js server using Express

const express = require("express");
const app = express();

const PORT = 3000;

// Root route
app.get("/", (req, res) => {
  res.send("Temporary Node.js server is running");
});

// Health check route
app.get("/health", (req, res) => {
  res.json({ status: "OK" });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

