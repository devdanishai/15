const express = require("express");
const { register, login, me } = require("../controllers/authController");
const protect = require("../middleware/auth");

const router = express.Router();

router.post("/register", (req, res, next) => register(req, res).catch(next));
router.post("/login", (req, res, next) => login(req, res).catch(next));
router.get("/me", protect, (req, res, next) => me(req, res).catch(next));

module.exports = router;