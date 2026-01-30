const express = require("express");
const cors = require("cors");
require("dotenv").config();

const connectDB = require("./config/db");
const todoRoutes = require("./routes/todoRoutes");
const errorHandler = require("./middleware/errorHandler");

const app = express();

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.send("Todo API running");
});

app.use("/api/todos", todoRoutes);

// last middleware
app.use(errorHandler);

async function start() {
  await connectDB();
  const port = process.env.PORT || 5000;
  app.listen(port, () => console.log(`Server running on ${port}`));
}

start().catch((err) => {
  console.error("Failed to start:", err);
  process.exit(1);
});