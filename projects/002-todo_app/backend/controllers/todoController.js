const Todo = require("../models/Todo");

exports.getTodos = async (req, res) => {
  const todos = await Todo.find({ user: req.user._id }).sort({ createdAt: -1 });
  res.json(todos);
};

exports.createTodo = async (req, res) => {
  const title = (req.body.title || "").trim();
  if (!title) return res.status(400).json({ message: "title is required" });

  const todo = await Todo.create({ title, user: req.user._id });
  res.status(201).json(todo);
};

exports.updateTodo = async (req, res) => {
  const { id } = req.params;

  const updates = {};
  if (typeof req.body.title === "string") updates.title = req.body.title.trim();
  if (typeof req.body.completed === "boolean") updates.completed = req.body.completed;

  // Only allow updating user's own todos
  const todo = await Todo.findOneAndUpdate(
    { _id: id, user: req.user._id },
    updates,
    { new: true }
  );
  if (!todo) return res.status(404).json({ message: "Todo not found" });

  res.json(todo);
};

exports.deleteTodo = async (req, res) => {
  const { id } = req.params;

  // Only allow deleting user's own todos
  const todo = await Todo.findOneAndDelete({ _id: id, user: req.user._id });
  if (!todo) return res.status(404).json({ message: "Todo not found" });

  res.json({ message: "Deleted" });
};