import express from "express";
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());

const items = [];

app.get("/items", (req, res) => {
  res.json(items);
});

app.post("/items", (req, res) => {
  const { name } = req.body || {};
  if (!name || typeof name !== "string") {
    return res.status(400).json({ error: "name is required" });
  }
  const item = { id: String(items.length + 1), name };
  items.push(item);
  res.status(201).json(item);
});

const port = process.env.PORT || 3001;
app.listen(port, () => {
  console.log(`Express API listening on http://localhost:${port}`);
});


