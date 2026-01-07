module.exports = {
  apps: [
    {
      name: "PM2Test",
      script: "index.js",
      env: {
        PORT: 3001,
        NODE_ENV: "development"
      },
      watch: true,
      autorestart: true
    }
  ]
};
