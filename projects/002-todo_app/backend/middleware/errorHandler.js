function errorHandler(err, req, res, next) {
    console.error(err);
  
    // common mongoose “bad id” case
    if (err.name === "CastError") {
      return res.status(400).json({ message: "Invalid id" });
    }
  
    res.status(500).json({ message: "Server error" });
  }
  
  module.exports = errorHandler;