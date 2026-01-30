const Todo = require("../models/Todo");

exports.getTodos = async (req, res) => {
  const todos = await Todo.find().sort({ createdAt: -1 });
  res.json(todos);
};

exports.createTodo = async (req, res) => {
  const title = (req.body.title || "").trim();
  if (!title) return res.status(400).json({ message: "title is required" });

  const todo = await Todo.create({ title });
  res.status(201).json(todo);
};

exports.updateTodo = async (req, res) => {
  const { id } = req.params;

  const updates = {};
  if (typeof req.body.title === "string") updates.title = req.body.title.trim();
  if (typeof req.body.completed === "boolean") updates.completed = req.body.completed;

  const todo = await Todo.findByIdAndUpdate(id, updates, { new: true });
  if (!todo) return res.status(404).json({ message: "Todo not found" });

  res.json(todo);
};

exports.deleteTodo = async (req, res) => {
  const { id } = req.params;

  const todo = await Todo.findByIdAndDelete(id);
  if (!todo) return res.status(404).json({ message: "Todo not found" });

  res.json({ message: "Deleted" });
};