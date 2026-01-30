const express = require("express");
const {
  getTodos,
  createTodo,
  updateTodo,
  deleteTodo
} = require("../controllers/todoController");

const router = express.Router();

router.get("/", (req, res, next) => getTodos(req, res).catch(next));
router.post("/", (req, res, next) => createTodo(req, res).catch(next));
router.put("/:id", (req, res, next) => updateTodo(req, res).catch(next));
router.delete("/:id", (req, res, next) => deleteTodo(req, res).catch(next));

module.exports = router;