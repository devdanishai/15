```bash
node -v
npm -v
mongod --version
sudo systemctl status mongod
```
## Backend
#### Initialize the backend
```bash
mkdir backend
cd backend
npm init -y
npm install express mongoose dotenv cors
npm install --save-dev nodemon
touch server.js
# write code for basic server.js or copy

touch .env 
# add following in .env file
# PORT=5000
# MONGO_URI=mongodb://127.0.0.1:27017/mern_local_db

# run server
npx nodemon server.js
```

##### Quick test of app:
`http://localhost:5000/`

## mongodb setup
```bash
mkdir models
touch models/user.js
# add code in file

mkdir routes
touch routes/userRoutes.js
# add code in file

# at the bottom of server.js add following line 
app.use("/api/users", require("./routes/userRoutes"));

# restart app
npx nodemon server.js
```
##### Quick test of app:
`http://localhost:5000/`

