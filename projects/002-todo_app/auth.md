### Goal
Add **JWT auth (register/login)** so each user has **their own todos** (private).

Below is the clean “by hand” order. Do **backend first**, then frontend.

---

### 1) Backend: install auth packages
In `projects/002-todo_app/backend`:

```bash
npm i bcryptjs jsonwebtoken
```

---

### 2) Backend: add new env variables
Edit `backend/.env` and add:

```env
JWT_SECRET=supersecret_change_me
JWT_EXPIRES_IN=7d
```

---

### 3) Backend: create `User` model
Create `backend/models/User.js`:

```js
const mongoose = require("mongoose");

const userSchema = new mongoose.Schema(
  {
    name: { type: String, required: true, trim: true },
    email: { type: String, required: true, unique: true, lowercase: true, trim: true },
    password: { type: String, required: true }
  },
  { timestamps: true }
);

module.exports = mongoose.model("User", userSchema);
```

---

### 4) Backend: create auth middleware (protect routes)
Create `backend/middleware/auth.js`:

```js
const jwt = require("jsonwebtoken");
const User = require("../models/User");

async function protect(req, res, next) {
  try {
    const header = req.headers.authorization || "";
    const [type, token] = header.split(" ");

    if (type !== "Bearer" || !token) {
      return res.status(401).json({ message: "Not authorized" });
    }

    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    const user = await User.findById(decoded.id).select("-password");
    if (!user) return res.status(401).json({ message: "Not authorized" });

    req.user = user;
    next();
  } catch (err) {
    return res.status(401).json({ message: "Not authorized" });
  }
}

module.exports = protect;
```

---

### 5) Backend: create auth controller
Create `backend/controllers/authController.js`:

```js
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const User = require("../models/User");

function signToken(userId) {
  return jwt.sign({ id: userId }, process.env.JWT_SECRET, {
    expiresIn: process.env.JWT_EXPIRES_IN || "7d",
  });
}

// POST /api/auth/register
exports.register = async (req, res) => {
  const name = (req.body.name || "").trim();
  const email = (req.body.email || "").trim().toLowerCase();
  const password = req.body.password || "";

  if (!name || !email || !password) {
    return res.status(400).json({ message: "name, email, password are required" });
  }

  const exists = await User.findOne({ email });
  if (exists) return res.status(409).json({ message: "Email already used" });

  const salt = await bcrypt.genSalt(10);
  const hashed = await bcrypt.hash(password, salt);

  const user = await User.create({ name, email, password: hashed });
  const token = signToken(user._id);

  res.status(201).json({
    token,
    user: { id: user._id, name: user.name, email: user.email },
  });
};

// POST /api/auth/login
exports.login = async (req, res) => {
  const email = (req.body.email || "").trim().toLowerCase();
  const password = req.body.password || "";

  if (!email || !password) {
    return res.status(400).json({ message: "email and password are required" });
  }

  const user = await User.findOne({ email });
  if (!user) return res.status(401).json({ message: "Invalid credentials" });

  const ok = await bcrypt.compare(password, user.password);
  if (!ok) return res.status(401).json({ message: "Invalid credentials" });

  const token = signToken(user._id);

  res.json({
    token,
    user: { id: user._id, name: user.name, email: user.email },
  });
};

// GET /api/auth/me (protected)
exports.me = async (req, res) => {
  res.json({ user: req.user });
};
```

---

### 6) Backend: create auth routes
Create `backend/routes/authRoutes.js`:

```js
const express = require("express");
const { register, login, me } = require("../controllers/authController");
const protect = require("../middleware/auth");

const router = express.Router();

router.post("/register", (req, res, next) => register(req, res).catch(next));
router.post("/login", (req, res, next) => login(req, res).catch(next));
router.get("/me", protect, (req, res, next) => me(req, res).catch(next));

module.exports = router;
```

---

### 7) Backend: connect auth routes in `server.js`
In `backend/server.js` add this line **near your other `app.use(...)`**:

```js
app.use("/api/auth", require("./routes/authRoutes"));
```

---

## ### 8) Backend: make todos “belong to a user”
### 8a) Update Todo model
Edit `backend/models/Todo.js` and add `user` field:

```js
user: { type: mongoose.Schema.Types.ObjectId, ref: "User", required: true },
```

So the schema becomes like:

```js
const todoSchema = new mongoose.Schema(
  {
    user: { type: mongoose.Schema.Types.ObjectId, ref: "User", required: true },
    title: { type: String, required: true, trim: true },
    completed: { type: Boolean, default: false }
  },
  { timestamps: true }
);
```

### 8b) Protect todo routes
Edit `backend/routes/todoRoutes.js`:
- import protect
- apply it to all routes

Example:

```js
const protect = require("../middleware/auth");

router.use(protect);
```

(put `router.use(protect);` after `const router = express.Router();`)

### 8c) Update todo controller logic to use `req.user._id`
Edit `backend/controllers/todoController.js`:

- **getTodos**: only return user’s todos

```js
const todos = await Todo.find({ user: req.user._id }).sort({ createdAt: -1 });
```

- **createTodo**: store user id

```js
const todo = await Todo.create({ title, user: req.user._id });
```

- **update/delete**: only allow if todo belongs to user  
Use `findOneAndUpdate` / `findOneAndDelete` with `{ _id: id, user: req.user._id }`.

---

### 9) Backend: test with curl (important)
Restart backend, then:

### Register
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"name":"A","email":"a@test.com","password":"123456"}'
```

Copy the returned `token`.

### Create todo (protected)
```bash
curl -X POST http://localhost:5000/api/todos \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{"title":"private todo"}'
```

If this works, backend auth is done.

---

# Frontend steps (after backend works)

### 10) Store token + attach token to axios
Update `frontend/src/api/todos.js`:
- keep `api = axios.create(...)`
- add interceptor to attach token from `localStorage`

```js
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});
```

### 11) Add auth API calls
Create `frontend/src/api/auth.js`:

```js
import axios from "axios";

const baseURL = "http://localhost:5000/api";

export async function registerUser(payload) {
  const res = await axios.post(`${baseURL}/auth/register`, payload);
  return res.data; // { token, user }
}

export async function loginUser(payload) {
  const res = await axios.post(`${baseURL}/auth/login`, payload);
  return res.data; // { token, user }
}

export async function fetchMe() {
  const token = localStorage.getItem("token");
  const res = await axios.get(`${baseURL}/auth/me`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return res.data; // { user }
}
```

### 12) Build simple Login/Register UI and only show Todo UI when logged in
You’ll:
- create `Login.jsx` + `Register.jsx` (or do it inside `App.jsx`)
- on success: `localStorage.setItem("token", token)`
- then load todos

---

### Before I give you the exact frontend UI code:
Do you want auth pages as:
- **A)** separate pages (simple routing), or
- **B)** just a single screen toggle (no routing, easiest)?